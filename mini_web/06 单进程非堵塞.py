# -*- coding: utf-8 -*-
import time
import socket
import sys
import re


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

        self.server_socket.setblocking(False)
        self.client_socket_list = list()

        self.documents_root = documents_root

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:

            # time.sleep(0.5)  # for test

            try:
                new_socket, new_addr = self.server_socket.accept()
            except Exception as ret:
                pass
                # print("-----1----", ret)  # for test
            else:
                new_socket.setblocking(False)
                self.client_socket_list.append(new_socket)

            for client_socket in self.client_socket_list:
                try:
                    request = client_socket.recv(1024).decode('utf-8')
                except Exception as ret:
                    pass
                    # print("------2----", ret)  # for test
                else:
                    if request:
                        self.recv(client_socket, request)
                    else:
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)

            # print(self.client_socket_list)

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
            response_headers += "\r\n"
            resopnse_body = f.read()
            f.close()
            clint_socket.send(response_headers.encode('utf-8'))
            # 再发送body
            clint_socket.send(resopnse_body)
            # 关闭套接字
            clint_socket.close()


# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    port = 7890
    http_server = WSGIServer(port, DOCUMENTS_ROOT)
    http_server.run_forever()


if __name__ == "__main__":
    main()
