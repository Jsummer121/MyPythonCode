# -*- coding: utf-8 -*-
import time

for i in range(101):
    num1 = i // 10 + 1
    print("\r" + "=" * num1 + ">" + "%.2f" % i + "%", end="")
    time.sleep(0.01)
