#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/8/23 22:20
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("login.html")

    def post(self):
        print(self.get_argument("user"))
        print(self.get_argument("psw"))
        self.write("登录成功")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/login", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


