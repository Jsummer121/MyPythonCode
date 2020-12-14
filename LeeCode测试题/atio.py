# -*- coding: utf-8 -*-


def myAtoi(s):
    s = s.lstrip()  # 去除左端空字符
    if s == "":
        return 0
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    a = ""
    for i in s:
        # 当是-的情况时
        if i == "-" and not a:  # 如果第一个是-
            a += i
        elif i == "-" and "-" in a:
            break
        elif i == "-" and "+" in a:
            break
        # 当是+的情况时
        elif i == "+" and not a:
            a += i
        elif i == "+" and "+" in a:
            break
        elif i == "+" and "-" in a:
            break
        elif i in num:
            a += i
        else:
            break

    if a == "" or a == "-" or a == "+":
        return 0

    a = int(a)

    if a < -2 ** 31:
        return -2147483648
    elif a > (2 ** 31) - 1:
        return 2147483647
    else:
        return a


if __name__ == '__main__':
    while True:
        print(myAtoi(input()))
