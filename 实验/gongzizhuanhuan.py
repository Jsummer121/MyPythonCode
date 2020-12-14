x=y=z=0
q=input()
x=q[0]
y=q[2:]
x=float(x)
y=float(y)
if x>=5:
    if y<=40:
        z=y*50
    else:
        z=2000+75*(y-40)
else:
    if y<=40:
        z=y*30.00
    else:
        z=1200+45*(y-40)
print('%.2f'%z)
