# -*- coding: utf-8 -*-
import threading
import time


def sing1():
    for i in range(5):
        print("I'm singing")


def sing2():
    for i in range(5):
        print("I'm singing")
        time.sleep(1)


def dance1():
    for i in range(5):
        print("I'm dancing")


def dance2():
    for i in range(5):
        print("I'm dancing")
        time.sleep(1)


def main():
    # 一般的不调用多线程的情况，先执行sing1函数，等sing1函数执行完之后，在运行dance1函数
    sing1()
    dance1()


def main_thread():
    """第二种多线程实现的方法"""
    # 这里的代码会先声明出5个线程，然后在开启线程，那么整个实现的效果就是5个print会在start调用之后一起打印出来
    for i in range(5):
        sing = threading.Thread(target=sing2)
        dance = threading.Thread(target=dance2)
        sing.start()
        dance.start()



if __name__ == '__main__':
    # main()
    main_thread()


# 说明
# 多线程创建之后，并不一定按start的执行顺序走，它是随机的，如果想要使得线程执行的顺序确定，那可以添加一个sleep。
