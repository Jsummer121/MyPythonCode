#!/usr/bin/env python

# 函数，排序，参数来决定正序还是逆序

li = [2, 8, 5, 4, 6]

li.reverse()
print("此处实现反转：", li)   # 不能实现逆序，只能实现反转

li.sort(reverse=True)
print("此处实现逆序:", li)
print(li.sort())    # None
print("此处实现正序:", li)

# 2.内置函数：sorted()/reversed()
li = [2, 8, 5, 4, 6, 1]

print("此处实现正序:", sorted(li))
print("此处实现反转：", list(reversed(li)))
print("此处实现逆序:", sorted(li, reverse=True))

