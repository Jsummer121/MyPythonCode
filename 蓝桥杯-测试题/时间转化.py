s = int(input())
h = s//(60**2)
m = (s-h*60**2)//60
s -= h*60**2+m*60
print('{}:{}:{}'.format(h,m,s))
