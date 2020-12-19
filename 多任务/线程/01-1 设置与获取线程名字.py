# -*- coding: utf-8 -*-
import threading
import time


def dance():
    print("I'm dancing")
    time.sleep(1)


if __name__ == '__main__':
    danc = threading.Thread(target=dance, name="跳舞")
    print(danc.getName())
    danc.setName("dance")
    print(danc.getName())
    danc.start()

