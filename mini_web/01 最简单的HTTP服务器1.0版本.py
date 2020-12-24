# -*- coding: utf-8 -*-
import socket


def recv(web_client):
    recv_data = web_client.recv(1024).decode("utf-8")
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)
    # 组织相应 头信息(header)
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"  # 用一个空的行与body进行隔开
    # 组织 内容(body)
    response_body = "Worker:summer"

    response = response_headers + response_body
    web_client.send(response.encode("utf-8"))
    web_client.close()


def main():
    # 创建套接字
    mini_web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    mini_web_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口
    mini_web_server.bind(("", 7890))
    # 主动改被动
    mini_web_server.listen(128)
    while True:
        # 接受相应
        web_client, clint_addr = mini_web_server.accept()
        # 返回参数
        recv(web_client)


if __name__ == '__main__':
    main()

