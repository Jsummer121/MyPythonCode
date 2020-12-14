a,b = map(int,input().split())
def go(n,total):
    if n == 1:
        return total
    for i in range(2,n+1):
        if n%i==0:
            total.append(i)
            return go(n//i,total)
        #if n%i== 0:
         #   total.append(i)
          #  n //= i
           # if n ==1:
            #    return total
            #else:
             #   return go(n,total)# 这个return是必须要有的，没有这个，go(4,[])进去的时候
#执行else语句，他不在有返回值，当一次次循环出来以后，整个结果是没有返回值的，因为就算确保
# n==1可以return，但是他的上面那一层接受这个返回值以后，就不在往他的父层返回参数，使得最后整个函数形成一个没有返回值的东西。
# 然后这个return不能每一次循环都返回，不然的话会导致所给的值淤积，因此得出结论：
#如果使用递归的时候，想要获得某个值，必须要return这个递归函数。当发现很多数据重复时
# 就要查看return这个函数放置的位置是否正确
def spl(a,b):
    for n in range(a,b+1):
        total = []# 存放输出
        s = go(n,total)
        s = list(map(str,s))
        s = '*'.join(s)
        print('{}={}'.format(n,s))
spl(a,b)
