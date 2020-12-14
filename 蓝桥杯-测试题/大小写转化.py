n = input()
s = []
for i in range(len(n)):
    if 64<ord(n[i])<91:
        s.append(chr(ord(n[i])+32))
    else:
        s.append(chr(ord(n[i])-32))
print(''.join(s))
