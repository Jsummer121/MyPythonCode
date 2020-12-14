n = int(input())
a=[[1]]
def tri(n):
    b=[1,1]
    if n != 1:
        for i in range(1,n):
            b.insert(i,a[n-1][i]+a[n-1][i-1])
    a.append(b)
for i in range(1,n):
    tri(i)
for i in range(len(a)):
    i = list(map(str,a[i]))
    print(' '.join(i))
