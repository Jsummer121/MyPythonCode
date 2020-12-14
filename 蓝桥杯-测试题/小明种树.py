N, M = input().split(' ')  # N表示棵树，M表示循环数 在后面输入的时候，输入的个数为M+1个
N, M = int(N), int(M)
a = {}
c = []
T = 0
# 循环接收后面每次循环的数，然后将其存到字典里面
for i in range(1, N+1):
    b = input().split(' ')
    a[i] = [int(x) for x in b]
    c.append(abs(sum(a[i][1:])))
    T += a[i][0] - c[i-1]

P = max(c)
k = c.index(P)
print(str(T)+' '+str(k+1)+' '+str(P))
""" T 苹果树总和
    k 果蔬最多的那一行
    P 个数为

73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0
"""