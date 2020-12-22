# -*- coding:utf-8 -*-
from multiprocessing import Process
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ' % (name, age))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    p = Process(target=run_proc, args=('test', 18), kwargs={"m": 20})
    p.start()
    print("------主线程执行完毕------")
