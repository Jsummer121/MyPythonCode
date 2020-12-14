a,b,c = map(int,input().split())
def minbeishu(a,b,c):
    s = [a*b,a*c,b*c,a*b*c]
    for i in range(4):
        d = min(s)
        if d%a == 0 and d%b==0 and d%c ==0:
            return d
        else:
            s.remove(d)
d = minbeishu(a,b,c)
print(d)


##############最大公约数
#a,b = map(int,input().split())
#def find_max(a,b):
#	c = min(a,b)
#	for i in range(c,1,-1):
#		if a%i ==0 and b%i==0:
#			return i
#c = find_max(a,b)
#print(c)
