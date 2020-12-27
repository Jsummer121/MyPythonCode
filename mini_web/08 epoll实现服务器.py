import socket
import re
import select


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, documents_root):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        self.documents_root = documents_root

        # 创建epoll对象
        self.epoll = select.epoll()
        # 将tcp服务器套接字加入到epoll中进行监听
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

        # 创建添加的fd对应的套接字
        self.fd_socket = dict()

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
            epoll_list = self.epoll.poll()

            # 对事件进行判断
            for fd, event in epoll_list:
                # 如果是服务器套接字可以收数据，那么意味着可以进行accept
                if fd == self.server_socket.fileno():
                    new_socket, new_addr = self.server_socket.accept()
                    # 向 epoll 中注册 连接 socket 的 可读 事件
                    self.epoll.register(new_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                    # 记录这个信息
                    self.fd_socket[new_socket.fileno()] = new_socket
                # 接收到数据
                elif event == select.EPOLLIN:
                    request = self.fd_socket[fd].recv(1024).decode("utf-8")
                    if request:
                        self.recv(self.fd_socket[fd], request)
                    else:
                        # 在epoll中注销客户端的信息
                        self.epoll.unregister(fd)
                        # 关闭客户端的文件句柄
                        self.fd_socket[fd].close()
                        # 在字典中删除与已关闭客户端相关的信息
                        del self.fd_socket[fd]

    def recv(self, clint_socket, recv_data):
        # 获取客户端发送的信息
        global f, response_headers
        # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
        request_header_line_0 = recv_data.splitlines()[0]

        # 从客户端发送的信息中获取客户端想要的资源
        get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
        # print("clint want file_name is %s" % get_file_name)

        if get_file_name == "/":
            file_name = self.documents_root + "/index.html"
        else:
            file_name = self.documents_root + get_file_name

        try:
            # 如果存在资源，将资源发送给对方
            f = open(file_name, "rb")
        except IOError:
            # 如果不存在资源，则发送404响应
            response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
            page_404 = self.documents_root + "/404.html"
            f = open(page_404, "rb")
        else:
            response_headers = "HTTP/1.1 200 OK\r\n"

        finally:
            resopnse_body = f.read()
            f.close()
            response_headers += "Content-Length: %d\r\n" % (len(resopnse_body))
            response_headers += "\r\n"

            clint_socket.send(response_headers.encode('utf-8'))
            # 再发送body
            clint_socket.send(resopnse_body)


# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    port = 7890

    # print("http服务器使用的port:%s" % port)
    http_server = WSGIServer(port, DOCUMENTS_ROOT)
    http_server.run_forever()


if __name__ == "__main__":
    main()
