x=input()
y=int(x)
if y==0:
    print('Speed: 0 - OK')
if 0<y<60:
    print('Speed: '+x+' - OK')
if y==60:
    print('Speed: 60 - OK')
if y>60:
    print('Speed: '+x+' - Speeding')
