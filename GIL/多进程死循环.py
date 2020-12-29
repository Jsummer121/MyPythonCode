# -*- coding: utf-8 -*-
import multiprocessing


def diemul():
    while True:
        pass


m1 = multiprocessing.Process(target=diemul)
m1.start()
while True:
    pass
