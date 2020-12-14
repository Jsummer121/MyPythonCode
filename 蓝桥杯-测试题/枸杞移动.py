# -*- coding: utf-8 -*-


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

if(sum(a) != sum(b)):
    print("-1")
elif(len(a) != len(b)):
    print("-1")
else:
    for i in range(1, N):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
        ans += abs(a[i - 1] - b[i - 1])
print(ans)
