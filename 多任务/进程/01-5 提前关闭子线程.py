# -*- coding: utf-8 -*-
import time
from multiprocessing import Process


def sing():
    while True:
        print("I'm singing")


def main():
    singing = Process(target=sing)
    singing.start()
    time.sleep(3)  # 主线程睡三秒之后，结束子线程
    singing.terminate()
    print("----主线程结束-----")


if __name__ == '__main__':
    main()
