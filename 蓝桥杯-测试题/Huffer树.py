num = input()
Hu = input().split()
Hu = list(map(int,Hu))
total = 0
while 1:
    tool = 0
    hu_min1 = min(Hu)
    Hu.remove(hu_min1)
    hu_min2 = min(Hu)
    Hu.remove(hu_min2)
    tool = hu_min1+hu_min2
    Hu.append(tool)
    total +=tool
    if len(Hu)==1:
        print(total)
        break
