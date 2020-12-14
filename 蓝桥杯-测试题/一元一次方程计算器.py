# -*- coding: utf-8 -*-

left_and = []
left_jian = []
right_and = []
right_jian = []

str = input()
# str = input()
left,right = str.split("=")#将输入的字符串根据=进行切片

# 左边把加法和减法分开
left_middle_and = left.split("+")#['3', '6a', '2', '2-1', '5', '7']
for i in left_middle_and:
    if "-" in i:
        left_middle_jian = i.split("-")
        left_and.append(left_middle_jian[0])
        for j in range(1,len(left_middle_jian)):
            left_jian.append(left_middle_jian[j])
    else:
        left_and.append(i)

# 右边把加法和减法分开
right_middle_and = right.split("+")
for i in right_middle_and:
    if "-" in i:
        right_middle_jian = i.split("-")
        right_and.append(right_middle_jian[0])
        for j in range(1,len(right_middle_jian)):
            right_jian.append(right_middle_jian[j])
    else:
        right_and.append(i)

number = 0
en_num = 0
weizhi = ""
# 循环判断四个列表里面是否存在未知数
for i in range(len(left_and)):
    num = left_and[i]
    if(num.isdigit()):
        number-=int(num)
    else:
        en_num+=int(num[:-1])
        weizhi = num[-1]

for i in range(len(left_jian)):
    num = left_jian[i]
    if(num.isdigit()):
        number+=int(num)
    else:
        en_num-=int(num[:-1])
        weizhi = num[-1]

for i in range(len(right_jian)):
    num = right_jian[i]
    if(num.isdigit()):
        number-=int(num)
    else:
        en_num+=int(num[:-1])
        weizhi = num[-1]

for i in range(len(right_and)):
    num = right_and[i]
    if (num.isdigit()):
        number += int(num)
    else:
        en_num -= int(num[:-1])
        weizhi = num[-1]

print(weizhi+"={:.3f}".format(number/en_num))
