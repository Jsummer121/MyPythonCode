# -*- coding: utf-8 -*-
import threading


def diethre():
    while True:
        pass


t1 = threading.Thread(target=diethre)
t2 = threading.Thread(target=diethre)
# t3 = threading.Thread(target=diethre)
# t4 = threading.Thread(target=diethre)
t1.start()
t2.start()
# t3.start()
# t4.start()
while True:
    pass
