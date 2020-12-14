# -*- coding: utf-8 -*-

"""
方法1：传入的字符串边list===list(map(int, input().split()))
先将输入的字符串切片，变成str类型的list类型，然后利用map函数将str类型变成int类型，最后利用list将迭代器变成list
方法2：字符串切片使用的是包前不包后并且使用:来进行切片，因此当输入的值等于列表长度时，需要使用[a:]方法
方法3：range类型也是利用迭代器创建一个包前不包后的迭代器。也需要特别注明
方法4：函数必须创建在使用函数代码之前
"""

# Qut用来存储所输出的值
Out = []
M, N = map(int, input().split())
List = list(map(int, input().split()))  # 将输入的字符串转化为整数类型的list


def Q(a, b):
    if (a == b):
        Out.append(List[a - 1])
    else:
        if (b == len(List)):
            list_Q = List[a - 1:]
        else:
            list_Q = List[a - 1:b]
        Out.append(sum(list_Q))


def C(a, b, c):
    for i in range(a - 1, b):
        List[i] += c


for i in range(N):
    str_list = input().split()
    # print(str_list)
    if (str_list[0] == "Q"):
        int1 = int(str_list[1])
        int2 = int(str_list[2])
        Q(int1, int2)
    else:
        int1 = int(str_list[1])
        int2 = int(str_list[2])
        int3 = int(str_list[3])
        C(int1, int2, int3)

for i in Out:
    print(i)
