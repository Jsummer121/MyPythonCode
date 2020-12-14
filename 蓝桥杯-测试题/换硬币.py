# -*- coding: utf-8 -*-

number = 0
List_total = []
N = int(input())
List = list(map(int, input().split()))
List.sort(reverse=True)
total = int(input())
List2 = [total//i for i in List]
# 确定第一行
for i in range(List2[0]+1):
    List_total.append(i * List[0]) # [0, 7, 14, 21]

# for i in range(1,N):
#     for k in range()
#     for j in range(List2[i]+1):
#         List_total.append(j*List[i])
print(List_total)
