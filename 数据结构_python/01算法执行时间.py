# -*- coding: utf-8 -*-
from timeit import Timer


# for a in range(1000):
#     for b in range(1000):
#         for c in range(1000):
#             if a + b + c == 1000:
#                 if a ** 2 + b ** 2 == c ** 2:
#                     print("a:{},b:{},c:{}".format(a, b, 1000 - a - b))


def test1():
    l = []
    for i in range(1000):
        l += [i]
        # l = l + [i]#此时的加效率是非常低的 一般不推荐


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


def test5():
    l = []
    for i in range(1000):
        l.extend([i])


def test6():
    l = []
    for i in range(1000):
        l.append(i)


def test7():
    l = []
    for i in range(1000):
        l.insert(0, i)


# 测试test1的运算时间
timer1 = Timer("test1()", "from __main__ import test1")
print("Timer1:", timer1.timeit(1000), "seonds")
# 测试test2的运算时间
timer2 = Timer("test2()", "from __main__ import test2")
print("Timer2:", timer2.timeit(1000), "seonds")
# 测试test3的运算时间
timer3 = Timer("test3()", "from __main__ import test3")
print("Timer3:", timer3.timeit(1000), "seonds")
# 测试test4的运算时间
timer4 = Timer("test4()", "from __main__ import test4")
print("Timer4:", timer4.timeit(1000), "seonds")
# 测试test5的运算时间
timer5 = Timer("test5()", "from __main__ import test5")
print("Timer5:", timer5.timeit(1000), "seonds")
# 测试test6的运算时间
timer6 = Timer("test6()", "from __main__ import test6")
print("Timer6:", timer6.timeit(1000), "seonds")
# 测试test7的运算时间
timer7 = Timer("test7()", "from __main__ import test7")
print("Timer7:", timer7.timeit(1000), "seonds")
