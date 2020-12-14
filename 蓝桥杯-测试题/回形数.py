m,n = map(int,input().split())
a = []# 整个矩阵
b = []# 用来存放回形数
c = []# 全为'A'的m行n列的数组
for i in range(m):
    a.append(input().split())
    c.append(['A' for i in range(n)])
def get_dom(row,col):
    if c == a:
        print(' '.join(b))
        return None
    elif a[row][col] == 'A':
        get_right(row-1,col+1)
    else:
        try:
            b.append(a[row][col])
            a[row][col] = 'A'
            row+=1
            get_dom(row,col)
        except:
            get_right(row-1,col+1)
def get_right(row,col):
    if c == a:
        print(' '.join(b))
        return None
    elif a[row][col] == 'A':
        get_up(row-1,col-1)
    else:
        try:
            b.append(a[row][col])
            a[row][col] = 'A'
            col+=1
            get_right(row,col)
        except:
            get_up(row-1,col-1)
def get_up(row,col):
    if c == a:
        print(' '.join(b))
        return None
    elif a[row][col] == 'A':
        get_left(row+1,col-1)
    else:
        try:
            b.append(a[row][col])
            a[row][col] = 'A'
            row-=1
            get_up(row,col)
        except:
            get_left(row+1,col-1)
def get_left(row,col):
    if c == a:
        print(' '.join(b))
        return None
    elif a[row][col] == 'A':
        get_dom(row+1,col+1)
    else:
        try:
            b.append(a[row][col])
            a[row][col] = 'A'
            col-=1
            get_left(row,col)
        except:
            get_dom(row+1,col+1)
get_dom(0,0)

#####################################################
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
