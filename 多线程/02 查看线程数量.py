# -*- coding: utf-8 -*-
import threading
import time


def sing():
    for i in range(5):
        print("singing")
        time.sleep(1)


def dance():
    for i in range(7):
        print("dancing")
        time.sleep(1)


def main():
    print(threading.enumerate())  # 该方法可以查看当前线程的数量
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    print(threading.enumerate())  # 这里打印出来的也只是一个主线程，因此可以知道在声明变量的是，线程并没有创建出来，只有在start函数调用之后，线程才开始创建。
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print("当前线程的数量为：", length)
        if length <= 1:
            break
        time.sleep(0.5)


if __name__ == '__main__':
    main()
