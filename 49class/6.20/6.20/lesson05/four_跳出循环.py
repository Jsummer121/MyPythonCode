#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/6/20 21:36

# 跳出循环break、continue
li = [1, 3, 5, 7, 9, 11, 2, 8]

i = 0
while i < len(li):
    if li[i] == 5:
        # break   # 跳出循环，程序终止，后面的将不再输出
        i += 1
        continue    # i值进入判断后，continue，推到while，而i值始终没有变化，再次进入判断，重复之前的动作，死循环
    if li[i] > 5:
        print(li[i])
    else:
        print(False)
    i += 1

# break跳出循环，程序终止
# continue跳出当前循环，进入下一次循环，注意：判断条件
print("="*20)
li = [1, 3, 5, 7, 9]
i = 0
while i < len(li):
    if li[i] == 5:
        i += 1
        continue
    print(li[i])
    i += 1
else:
    print('----end----')
# else可以跟在while的后面，但是只有循环结束才会执行else，如果循环是被break掉的，那么这个else就不会执行

