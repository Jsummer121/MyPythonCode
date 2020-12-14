m,n = map(int,input().split())
numpy = []
c = [[0 for i in range(m)] for y in range(m)]
#如果c放外面会导致c里面的元素不会清零，因此会使整个值变得非常大，远离正常值
#
#
for i in range(m):
    numpy.append(list(map(int,input().split())))
def juzhengchengfa(numpy_1,numpy_2,m):
    #c = [[0 for i in range(m)] for y in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j] += numpy_1[i][k]*numpy_2[k][j]
    return c
numpy_1=numpy.copy()
if n == 0:
    for i in range(m):
        for j in range(m):
            if i==j:
                numpy_1[i][j] = 1
            else:
                numpy_1[i][j] = 0
else:
    for i in range(n-1):
        print(numpy_1)
        numpy_1 = juzhengchengfa(numpy_1,numpy,m)
for i in range(m):
    print('{}'.format(' '.join(list(map(str,numpy_1[i])))))
