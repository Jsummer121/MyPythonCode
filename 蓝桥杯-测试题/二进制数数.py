# 输入两个整数
# 利用range进行循环
# 利用bin函数求每个整数的二进制并且切割
# 利用count函数查看1在字符串内部的个数并进行相加
# 返回总数
a,b = map(int,input().split())
count = 0
for i in range(a,b+1):
    x = bin(i)[2:]
    count+=x.count('1')
print(count)
