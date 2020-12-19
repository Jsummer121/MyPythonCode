# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, people, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.people = people

    def run(self):
        print("这是%s的线程" % self.people)
        time.sleep(1)
        print("bye")


if __name__ == '__main__':
    t1 = MyThread("summer")
    t1.start()
