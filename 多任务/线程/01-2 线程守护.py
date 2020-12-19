# -*- coding: utf-8 -*-
import threading
import time


def dance():
    print("I want dance two hour")
    time.sleep(60*2)
    print("2h 跳舞结束")


if __name__ == '__main__':
    danc = threading.Thread(target=dance)
    danc.setDaemon(True)  # 为该线程设置线程守护
    danc.start()
    time.sleep(5)  # 主线程睡5s
    print("主线程执行完毕")
