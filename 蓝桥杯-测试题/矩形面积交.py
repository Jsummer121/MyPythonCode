x1,y1,x2,y2 = map(float,input().split())
x3,y3,x4,y4 = map(float,input().split())
if x1>x2:
    x1,x2 = x2,x1
if y1>y2:
    y1,y2 = y2,y1
if x3>x4:
    x3,x4 = x4,x3
if y3>y4:
    y3,y4 = y4,y3
temp_x1 = max(x1,x3)
temp_x2 = min(x2,x4)
temp_y1 = max(y1,y3)
temp_y2 = min(y2,y4)
if temp_x2 - temp_x1 <0 or temp_y2 - temp_y1 <0:
    res = 0
else:
    res = (temp_y2-temp_y1)*(temp_x2-temp_x1)
print('{:.2f}'.format(res))
