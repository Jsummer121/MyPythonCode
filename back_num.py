import math
m, n = map(int, input().split())
res = []
for i in range(m):
    res.append(input().split())
N = math.ceil(min(m, n) / 2)
result = []
num = 0
for loop in range(N):
    for x in range(loop, m - loop):
        result.append(res[x][loop])
    for y in range(loop + 1, n - loop):
        result.append(res[m - 1 - loop][y])
        # 下面是逆方向
    if n - 1 > 2 * loop:
        for p in range(m - loop - 2, loop - 1, -1):
            result.append(res[p][n - 1 - loop])
    if m - 1 > 2 * loop:
        for q in range(n - loop - 2, loop, -1):
            result.append(res[loop][q])
print(' '.join(result))

    # 1 2 1 9 8 7 6
    # 2 3 5 4 3 2 5
    # 3 4 6 7 8 1 4
    # 4 5 6 7 8 9 3
    # 5 6 7 8 9 1 2


# 1 2
# 3 4
# 5 6
# 7 8
# 9 1

# m=5 n=2




