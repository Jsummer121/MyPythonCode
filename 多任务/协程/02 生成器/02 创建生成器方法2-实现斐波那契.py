# -*- coding: utf-8 -*-


def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
    return 'done'


F = fib(5)

# print(next(F))
# print(next(F))
# print(next(F))
# print(next(F))
# print(next(F))
# print(next(F))  # StopIteration: done

# for i in fib(5):
#     print(i)

f = fib(5)

while True:
    try:
        x = next(f)
        print("values:%d"%x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break
