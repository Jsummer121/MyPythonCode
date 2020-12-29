# -*- coding: utf-8 -*-
import multiprocessing


def diemul():
    while True:
        pass


if __name__ == '__main__':
    m1 = multiprocessing.Process(target=diemul)
    # m2 = multiprocessing.Process(target=diemul)
    # m3 = multiprocessing.Process(target=diemul)
    # m4 = multiprocessing.Process(target=diemul)
    m1.start()
    # m2.start()
    # m3.start()
    # m4.start()
    while True:
        pass
