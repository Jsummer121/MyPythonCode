n = input().split()
a,b = (int(n[0]),int(n[1]))
sample = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen'}
ten = {0:'zero', 10:'ten', 20:'twenty',30:'thirty',40:'forty',50:'fifty'}
def time(i):
    if i%10 == 0:
        return ten[i]
    elif i < 20:
        return sample[i]
    else:
        return ten[i//10*10]+' '+sample[i%10]
if b == 0:
    time_b = "o'clock"
else:
    time_b =time(b)
print('{} {}'.format(time(a),time_b))
