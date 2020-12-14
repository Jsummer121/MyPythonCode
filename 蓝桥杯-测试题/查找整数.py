n = input()
s = input().split()
ind = int(input())
s = list(map(int,s))
try:
    num = s.index(ind)+1
    print(num)
except:
    print(-1)

