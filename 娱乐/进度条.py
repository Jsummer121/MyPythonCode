# -*- coding: utf-8 -*-
import time

for i in range(100):
    num = i // 10 + 1
    print("\r" + "=" * num + ">", end="")
    time.sleep(0.01)
