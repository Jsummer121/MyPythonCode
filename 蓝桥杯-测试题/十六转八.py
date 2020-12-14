n = int(input())
z = []
for i in range(n):
    m = input()
    m = int(m,16)
    z.append(oct(m)[2:])
for i in z:
    print(i)
