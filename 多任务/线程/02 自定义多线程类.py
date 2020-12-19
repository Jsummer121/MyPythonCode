# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            self.test1(i)
            self.test2(i)
            msg = "I'm "+self.name+" @ "+str(i)
            print(msg)

    def test1(self, i):
        print("这是测试1的第%s次" % str(i))

    def test2(self, i):
        print("这是测试2的第%s次" % str(i))


if __name__ == '__main__':
    t = MyThread()
    t.start()
