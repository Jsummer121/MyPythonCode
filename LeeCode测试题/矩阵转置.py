# -*- coding: utf-8 -*-


def turn(n):
    N = len(n)
    M = len(n[0])
    num = []
    for i in range(M):
        num1 = []
        for j in range(N):
            num1.append(n[j][i])
        num.append(num1)
    return num


if __name__ == '__main__':
    n = [[1, 2], [3, 4], [5, 6]]
    print(turn(n))
