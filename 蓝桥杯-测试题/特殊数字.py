for i in range(100,1000):
    a = list(map(int,list(str(i))))
    if a[0]**3+a[1]**3+a[2]**3==i:
        print(i)
