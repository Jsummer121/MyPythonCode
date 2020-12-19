# -*- coding: utf-8 -*-
import threading
import time


def dance():
    print("I want dance 2s")
    time.sleep(2)
    print("跳舞完毕")


def sing():
    print("I want sing 3s")
    time.sleep(3)
    print("唱歌完毕")


if __name__ == '__main__':
    print("主线程开始")
    danc = threading.Thread(target=dance)
    sing = threading.Thread(target=sing)
    danc.start()
    sing.start()
    danc.join()
    sing.join()
    print("主线程执行完毕")

# 注：
# 添加阻塞即使得主线程与最后一个子线程一起结束
