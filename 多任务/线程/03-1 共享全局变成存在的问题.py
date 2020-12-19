# -*- coding: utf-8 -*-
from threading import *
import time

total_ticket = 100


class MyWindow(Thread):
    def run(self) -> None:
        global total_ticket
        while total_ticket > 0:
            time.sleep(0.2)  # 模拟人工操作的延时
            total_ticket -= 1
            print("还剩%d张票" % total_ticket)


if __name__ == '__main__':
    t1 = MyWindow()
    t2 = MyWindow()
    t3 = MyWindow()
    t4 = MyWindow()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
