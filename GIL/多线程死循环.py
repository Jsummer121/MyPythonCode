# -*- coding: utf-8 -*-
import threading


def diethre():
    while True:
        pass


t1 = threading.Thread(target=diethre)
t1.start()
while True:
    pass
