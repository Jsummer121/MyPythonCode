# -*- coding: utf-8 -*-
from multiprocessing import Process
import os


def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
    # 在主进程中打出子进程的pid
    print("子进程的pid为：%d" % p.pid)
    p.join()
    print("-----主进程结束-----")
