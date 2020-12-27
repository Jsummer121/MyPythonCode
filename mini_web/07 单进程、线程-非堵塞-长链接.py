# -*- coding: utf-8 -*-
import re
import socket

# 这里配置服务器
DOCUMENTS_ROOT = "./html"


def recv(clint_socket, recv_data):
    # 获取客户端发送的信息
    global f, response_headers
    # print(recv_data)    # 获取该信息的第一行GET / HTTP/1.1
    request_header_line_0 = recv_data.splitlines()[0]

    # 从客户端发送的信息中获取客户端想要的资源
    get_file_name = re.match(r"[^/]+(/[^ ]*)", request_header_line_0).group(1)
    # print("clint want file_name is %s" % get_file_name)

    if get_file_name == "/":
        file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        file_name = DOCUMENTS_ROOT + get_file_name

    try:
        # 如果存在资源，将资源发送给对方
        f = open(file_name, "rb")
    except IOError:
        # 如果不存在资源，则发送404响应
        response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
        page_404 = DOCUMENTS_ROOT + "/404.html"
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


def main():
    # 创建套接字
    http_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    http_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    http_socket_server.bind(("", 7890))
    # 改主动为被动
    http_socket_server.setblocking(False)
    http_socket_server.listen(128)
    clint_socket_list = list()
    # 接受客户端响应
    while True:
        try:
            new_socket, clint_addr = http_socket_server.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            clint_socket_list.append(new_socket)

        for clint_socket in clint_socket_list:
            try:
                # 数据处理
                recv_data = clint_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if recv_data:
                    recv(clint_socket, recv_data)
                else:
                    clint_socket.close()
                    clint_socket_list.remove(clint_socket)
                    # print(clint_socket, "已经关闭")


if __name__ == '__main__':
    main()
