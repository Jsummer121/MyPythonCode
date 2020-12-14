## Random库

random库是使用随机数的Python标准库

伪随机数：采用梅森旋转算法可以生成伪随机序列中元素

生成随机数：

给定随机数种子-》采用梅森旋转算法-》随机序列

**基本随机函数**：seed(),random()

**扩展随机函数**：randint(),randrange(),getrandbit(),ubiform(),choice(),shuffle()

## seed（a=none）

**描述**：初始化给定的随机数种子，默认为当前系统的时间

`random.seed(10)`产生种子10对应的序列

## random()

**描述**：生成一个[0.0,1.0)之间的随机小数

`random.random()`

> 0.9469572481012325

可以利用seed来控制random生成的随机数

```
>>> import random
>>> random.random()
0.9469572481012325
>>> random.random()
0.2735506429592328
>>> random.seed(10)
>>> random.random()
0.5714025946899135
>>> random.seed(10)
>>> random.random()
0.5714025946899135
>>> random.seed(7)
>>> random.random()
0.32383276483316237
>>> random.seed(7)
>>> random.random()
0.32383276483316237
```

## randint（a，b）

生成一个[a,b]之间的整数

`random.randint(10,100)`

> 64

## randrange(m,n[,k])

生成一个[m,n)之间以k为步长的随机整数

`randint.randrange(10,100,10)`

> 80

## getrandbits(k)

生成一个k比特长度的随机整数

`random.getrandbits(2)`
0或1或2或3

## uniform(a,b)

生成[a,b]之间的随机小数

`random.uniform(4,6)`
4.429396361671324

## choice(seq)

从序列seq中随机选取一个元素

`random.choice([1,2,3,4,5,6])`
1

## shuffle(seq)

将序列seq中元素随机排列，然后返回打乱后的序列

```
>>>s = [1,2,15,6,4,3,3,6,3,3]
>>>random.shuffle(s)
>>>s
[4, 15, 3, 3, 6, 2, 3, 3, 1, 6]
```

