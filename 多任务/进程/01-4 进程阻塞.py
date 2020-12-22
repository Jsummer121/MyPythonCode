# -*- coding: utf-8 -*-
import time
from multiprocessing import Process


def dance(n):
    for i in range(n):
        print("----这是第%s次执行子进程----" % i)
        time.sleep(0.1)


def main():
    p1 = Process(target=dance, args=(10, ))
    p1.start()  # 开启线程
    print("---主线程在阻塞前---")
    p1.join()
    print("---主线程在阻塞后---")


if __name__ == '__main__':
    main()
