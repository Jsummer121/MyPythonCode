# -*- coding: utf-8 -*-

List = []
N = int(input())


def and_7(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total % 7


def Find_7(number):
    if ("7" in str(number)):
        return 0
    elif (number % 7 == 0):
        return 0
    elif (and_7(number) == 0):
        return 0
    else:
        return number


for i in range(N):
    number = 0
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        number += Find_7(j) ** 2
    List.append(number % (10 ** 9 + 7))
for i in List:
    print(i)
