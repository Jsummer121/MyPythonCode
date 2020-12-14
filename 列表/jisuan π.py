a=float(input())
c=1
f=n=0
def b(n):
    e=1
    if n==0:
        return 1
    else:
        m=range(n+1)
        for i in m[1:]:
            e*=i
    global c
    c=c*(2*n+1)
    return e/c
while a<b(n):
    f+=b(n)
    n+=1
f*=2
print('%.6f'%f)
