import random
n=int(input('请输入一个小于8正整数:'))
print('您要祖成一个'+str(n)+'阶矩阵')
L=range(n+1)[1:]
S=list(L)                         #阶层数的列表：S（用来计算t）
f=1                                #总子函数个数：f
D=N=t=k=m=j=i=o=q=e=0              #整个值：D,子元素的乘积：N,逆序数：t
p=''                               #单个个数来求t
J=[]                               #整个矩阵：J
A=[]                               #单行矩阵
P=[]                               #第二个数值的排列
for i in L:
    f*=i  
for i in L:
    for i in L:
        A+=[random.randint(0,100)]
    J+=[A]
    A=[]                           #整个矩阵用二维数组表示
print('随机产生的'+str(n)+'阶阶层为:'+str(J))
if n==1:
    D=J[0][0]
if n==2:
    D=J[0][0]*J[1][1]-J[0][1]*J[1][0]
if n==3:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            k=Y[0]
            p=str(i)+str(j)+str(k)
            P.append(p)
    for i in range(f):
        t=0
        if P[i][1]<P[i][0]:
            t+=1
        if P[i][2]<P[i][0]:
            t+=1
        if P[i][2]<P[i][1]:
            t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]
if n==4:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            for k in Y:
                q=Y.index(k)
                I=Y[0:q]+Y[q+1:]
                m=I[0]
                p=str(i)+str(j)+str(k)+str(m)
                P.append(p)
    for i in range(f):
        t=0
        for j in range(1,n):
            for k in range(j):
                if P[i][j]<P[i][k]:
                    t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]*J[3][int(P[i][3])-1]
if n==5:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            for k in Y:
                q=Y.index(k)
                I=Y[0:q]+Y[q+1:]
                for m in I:
                    e=I.index(m)
                    Q=I[0:e]+I[e+1:]
                    v=Q[0]
                    p=str(i)+str(j)+str(k)+str(m)+str(v)
                    P.append(p)
    for i in range(f):
        t=0
        for j in range(1,n):
            for k in range(j):
                if P[i][j]<P[i][k]:
                    t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]*J[3][int(P[i][3])-1]*J[4][int(P[i][4])-1]
if n==6:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            for k in Y:
                q=Y.index(k)
                I=Y[0:q]+Y[q+1:]
                for m in I:
                    e=I.index(m)
                    Q=I[0:e]+I[e+1:]
                    for v in Q:
                        h=Q.index(v)
                        X=Q[0:h]+Q[h+1:]
                        x=X[0]
                        p=str(i)+str(j)+str(k)+str(m)+str(v)+str(x)
                        P.append(p)
    for i in range(f):
        t=0
        for j in range(1,n):
            for k in range(j):
                if P[i][j]<P[i][k]:
                    t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]*J[3][int(P[i][3])-1]*J[4][int(P[i][4])-1]*J[5][int(P[i][5])-1]                
if n==7:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            for k in Y:
                q=Y.index(k)
                I=Y[0:q]+Y[q+1:]
                for m in I:
                    e=I.index(m)
                    Q=I[0:e]+I[e+1:]
                    for v in Q:
                        h=Q.index(v)
                        X=Q[0:h]+Q[h+1:]
                        for x in X:
                            c=X.index(x)
                            Z=X[0:c]+X[c+1:]
                            z=Z[0]
                            p=str(i)+str(j)+str(k)+str(m)+str(v)+str(x)+str(z)
                            P.append(p)
    for i in range(f):
        t=0
        for j in range(1,n):
            for k in range(j):
                if P[i][j]<P[i][k]:
                    t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]*J[3][int(P[i][3])-1]*J[4][int(P[i][4])-1]*J[5][int(P[i][5])-1]*J[6][int(P[i][6])-1]
if n==8:
    for i in S:
        O=S[0:i-1]+S[i:]
        for j in O:
            o=O.index(j)
            Y=O[0:o]+O[o+1:]
            for k in Y:
                q=Y.index(k)
                I=Y[0:q]+Y[q+1:]
                for m in I:
                    e=I.index(m)
                    Q=I[0:e]+I[e+1:]
                    for v in Q:
                        h=Q.index(v)
                        X=Q[0:h]+Q[h+1:]
                        for x in X:
                            c=X.index(x)
                            Z=X[0:c]+X[c+1:]
                            for z in Z:
                                b=Z.index(z)
                                V=Z[0:b]+Z[b+1:]
                                y=V[0]
                                p=str(i)+str(j)+str(k)+str(m)+str(v)+str(x)+str(z)+str(y)
                                P.append(p)
    for i in range(f):
        t=0
        for j in range(1,n):
            for k in range(j):
                if P[i][j]<P[i][k]:
                    t+=1
        D+=(-1)**t*J[0][int(P[i][0])-1]*J[1][int(P[i][1])-1]*J[2][int(P[i][2])-1]*J[3][int(P[i][3])-1]*J[4][int(P[i][4])-1]*J[5][int(P[i][5])-1]*J[6][int(P[i][6])-1]*J[7][int(P[i][7])-1]
print('随机产生的阶层的值为'+str(D))