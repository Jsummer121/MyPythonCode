# -*- coding: utf-8 -*-

List = []
while (True):
    try:
        m, A, B = map(int, input().split())
        number = A * B
        if (m == 2):
            List.append(bin(number)[2:])
        elif (m == 8):
            List.append(oct(number)[2:])
        else:
            str1 = ""
            while (True):
                if (number < m):
                    str1 = str(number) + str1
                    List.append(str1)
                    break
                else:
                    a = number % m
                    number //= m
                    str1 = str(a) + str1
    except:
        for i in List:
            print(i)
        break
