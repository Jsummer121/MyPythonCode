x=input()
y=z=j=0
for i in x:
    if i==' ':
        j+=1   
z=''
a=[]
if x==len(x)*' ':
    print('')
    x=''
def p(x):
    for i in range(len(x)):
        u=0
        while x[0]==' ':
            x=x[1:]
        if x[i]==' ':
           return i
if x:
  while x[0]==' ':
     x=x[1:]
  while x[-1]==' ':
    x=x[:-1]
  for i in range(j):
    y=p(x)
    if y:
        z=x[:y]
        x=x[y+1:]
        while x[0]==' ':
            x=x[1:]
        a.append(z)    
  a.append(x)
  a.reverse()
  a=' '.join(a)
  print(a)
