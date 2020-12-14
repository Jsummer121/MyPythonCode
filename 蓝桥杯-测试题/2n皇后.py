n = int(input())
a = []  # 总棋盘
temp_W = [None for i in range(n)]  # 临时存放白皇后位置
temp_B = [None for j in range(n)]  # 临时存放黑皇后的位置
total = 0  # 总次数
for i in range(n):
    a.append(input().split())


def check_W(temp_W, row):  # 查看白皇后所在位置是否合法：是否是1，是否在对角线上，是否在同一列
    if a[row][temp_W[row]] == '1':
        for j in range(row):
            if abs(j - row) == abs(temp_W[j] - temp_W[row]) or temp_W[j] == temp_W[row]:
                return False
        return True


def check_B(temp_B, row, temp_W):  # 查看黑皇后所在位置是否合法：是否是1，是否在对角线，是否在之前黑皇后的同一列，是否白皇后已存在
    if a[row][temp_B[row]] == '1' and temp_W[row] != temp_B[row]:
        for i in range(row):
            if abs(i - row) == abs(temp_B[row] - temp_B[i]) or temp_B[i] == temp_B[row]:
                return False
        return True


def find_W(temp_W, row):
    if row == n:
        find_B(temp_B, 0)
    else:
        for col in range(n):
            temp_W[row] = col
            if check_W(temp_W, row):
                find_W(temp_W, row + 1)


def find_B(temp_B, row):
    global total
    if row == n:
        total += 1
        return
    else:
        for col in range(n):
            temp_B[row] = col
            if check_B(temp_B, row, temp_W):
                find_B(temp_B, row + 1)


find_W(temp_W, 0)
print(str(total))
