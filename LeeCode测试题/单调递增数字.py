# -*- coding: utf-8 -*-


def monotoneIncreasingDigits(N):
    str_N = str(N)
    num = list(str_N)
    flag = len(str_N)
    for i in range(len(str_N)-1,0,-1):
        if num[i-1] > num[i]:
            num[i - 1] = str(int(num[i - 1]) - 1)
            flag = i
    num = "".join(num)
    return int(num[:flag] + '9' * (len(num) - flag))


if __name__ == '__main__':
    N = "20"
    print(monotoneIncreasingDigits(N))
