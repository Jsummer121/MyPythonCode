m = int(input())
s = []
for a in range(1,10):
    for b in range(0,10):
        c = m-2*a-2*b
        if c<10:
            s.append('{}{}{}{}{}'.format(a,b,c,b,a))
        elif 10<c<20 and c%2==0:
            c = int(c/2)
            s.append('{}{}{}{}{}{}'.format(a,b,c,c,b,a))
s = sorted(list(map(int,s)))
for i in range(len(s)):
    print(s[i],end='\r\n')
