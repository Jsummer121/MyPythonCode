# lambda-匿名函数

An anonymous inline function consisting of a single [expression](mk:@MSITStore:E:\summer\Doc\Python372.chm::/glossary.html#term-expression) which is evaluated when the function is called.  The syntax to create a lambda function is `lambda [parameters]: expression`

一种匿名内联函数，由一个单独的内联函数组成，在调用该函数时对其求值。创建lambda函数的语法是`lambda 参数名:表达式`

## 1.简单入门

一个简单的return函数

```
def a():
	return 123
a = a()
print(a)
>>> 123
```

在python中，要想一下子写一个简单的函数，我们就可以用到lambda。

```
a = lambda:123
a = a()
print(a)
>>>123
```

## 2.带参数的函数

```
def fun(a,b):
	return a+b
c = fun(1,2)
print(c)
>>>3
```

同样的方法，我们只要在`:`左边加上我们要传入的参数，在右边进行返回值的表达就行了

```
fun = lambda a,b:a+b
c = fun(1,2)
print(c)
>>>3
```

## 3.运用filter制作筛选函数

```
li = [1,8,5,3,9,5,7,9,6,4,6,3,12]
print(list(filter(lambda a:a>6,li))
>>> [8, 9, 7, 9, 12]
```

上面的代码可以帮助我们筛选出列表中函数大于6的整数

## 4.自制一个简单的方法函数

```
def test(a,b,func):
	res = func(a,b)
	return res

num = test(5,6,lambda a,b:a+b)
print("加法：",num)
num = test(5,6.lammbda a,b:a-b)
print("减法："num)
>>>
加法: 11
减法: -1
```

## 5.实现匿名函数的输入

```
func = input("请输入一个匿名函数")
print(func) 	 # 'lambda a,b:a+b'
print(type(func))# <class 'str'>
func = eval(func)
print(type(func))# <class 'function'>注意：这个地方千万不能加小括号，带小括号就表明是运行这个函数。但此时func还是str，是无效的。
num = test(11,12,func)# 如果是两个参数的匿名函数可用
print(num)		 # 23
```

## 6.实现输入函数循环执行

```
while True:
    flag = input("继续吗？如果继续请输入y，其他结束")
    if flag.lower() == 'y':
        func = input("请输入一个匿名函数：")
        func = eval(func)
        num = test(11, 22, func)
        print(num)
    else:
        print("结束运行")
        break
```

