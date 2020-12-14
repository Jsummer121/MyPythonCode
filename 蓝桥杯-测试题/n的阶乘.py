n = int(input())
def n_n(n):
    a = [1]
    for i in range(1,n+1):
        a = [x*i for x in a]
        while 1: 
            for z in range(len(a)):
                if a[z] >10:
                    try:
                        a[z+1] += a[z]//10
                    except:
                        a.append(a[z]//10)
                    a[z] %= 10
            b=0
            for z in range(len(a)):
                if a[z] > 10:
                    b+=1
            if b == 0:
                break
    return a
a = n_n(n)[::-1]
a = list(map(str,a))
a = ''.join(a)
print(a)

    
