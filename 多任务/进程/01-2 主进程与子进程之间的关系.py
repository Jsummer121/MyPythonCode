# -*- coding: utf-8 -*-
from multiprocessing import Process
import time


def run_proc():
    """子进程要执行的代码"""
    while True:
        print("----2----")
        time.sleep(1)


def main():
    p = Process(target=run_proc)
    p.start()
    # 1.主进程提前结束，则所有子进程也跟着一起结束，如果主进程代码执行完，会等所有子进程结束之后再结束
    print("-----主进程结束------")


if __name__ == '__main__':
    main()
