# 第一种
# L=[1,2,3,4,5,6,7,8,9]
# for x in L:
#     for y in range(x):
#         z=y+1
#         if x==z==9:
#             print('9*9=81');break
#         elif x==z:
#             print(z,'*',x,'=',x*z,end='\n')
#         elif z+1==x==3:
#             print(z,'*',x,'=',x*z,end='  ')
#         elif z+2==x==4:
#             print(z,'*',x,'=',x*z,end='  ')
#         else:
#             print(z,'*',x,'=',x*z,end=' ')

#第二种
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')
        if i == j:
            print()
        
