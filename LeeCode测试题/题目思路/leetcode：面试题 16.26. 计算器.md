# Python:面试题 16.26. 计算器

&nbsp;&nbsp;&nbsp;&nbsp;题目地址：Leetcode[面试题 16.26. 计算器](https://leetcode-cn.com/problems/calculator-lcci/)

给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。表达式仅包含非负整数，+， - ，*、/ 四种运算符和空格  。 整数除法仅保留整数部分。

##### 示例1

```
输入: "3+2*2"
输出: 7
```

##### 示例2

```
输入: " 3/2 "
输出: 1
```

##### 示例3

```
输入: " 3+5 / 2 "
输出: 5
```

## 方法一、

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;第一种：python内置函数`eval()`方法适合在平时自己写代码玩的时候可以使用，在leedcode上或者面试的时候，一般都被舍弃了。

代码也比较简洁，一行走完：

```python
return int(eval(s))
```

## 方法二、

&nbsp;&nbsp;&nbsp;&nbsp;第二种方法运用正常的一个思路，首先使用一个栈，用来存放每个数字。然后一个一个的遍历整个字符串，如果这个值为数字，那么就将该值压入栈内，如果该值是符号，那么进行相应的标注，直到遍历完整个字符串，此时栈中已经放了所有的值，然后返回整个栈的数字之和即可。

##### 大致思路：

1. 寻找一个中间键，用来存放每一个数。这里因为需要经常性的进行放入元素和删除元素并且又是始终在一端，我们可以运用栈来存储值。命名为：stack。
2. 利用flag来查看在前面的匹配中是否匹配到了“-”号，利用pre来存储前面匹配到的“*”号或者“/”号。
3. 利用number来收集数字，因为并不是每个值都为个位数，需要根据下一个终止符(即四个运算符号)来结束number的增加。
4. 下面的操作即一次循环字符串的每一个值：
   1. 如果索引到的值为空白字符，则继续下一个搜索。
   2. 如果索引到的这个值为“-”我们进行下面的判断（为什么要第一个查找-？因为“-”号比较特殊，有“-”不一定需要进行数值计算，比如3/-2。此时的-号是用来定义数字的，并不是一个终止符）：
      1. 如果扫描到了“-”，但是前面并没有数字，说明这个“-”是用来定义数字的（即起到将1变成-1的作用）那么直接将判断正负的flag变成负即可
      2. 如果存在数字，说明这个“-”是一个终止符，我们就需要进行值的计算了：
         1. 首先判断flag的正负，然后根据这个来决定number的正负，此时不需要转换flag的值，因为判断为“-”，肯定需要进行flag赋值为False
         2. 如果前面不存在pre（例如5-1），那么直接将这个number压入栈
         3. 否则从栈中退出一个元素（是“/”或“*”前面的数字），然后根据pre的类型，进行相应的计算
         4. 当执行完上面的操作之后，将number变成0。然后因为扫描到的字符是“-”，所以应该将flag变成Flase
   3. 如果索引到的值为“+”：
      1. 首先判断flag的正负，然后根据这个来决定number的正负，如果flag是False，在转换完成以后需要将flag变成True
      2. 如果前面不存在pre（例如5+1），那么直接将这个number压入栈
      3. 否则从栈中退出一个元素（是“/”或“*”前面的数字），然后根据pre的类型，进行相应的计算
      4. 当执行完上面的操作之后，将number变成0
   4. 如果索引到的值为“*”：
      1. 首先判断flag的正负，然后根据这个来决定number的正负，如果flag是False，在转换完成以后需要将flag变成True
      2. 如果前面不存在pre（例如5*1），那么直接将这个number压入栈
      3. 否则从栈中退出一个元素（是“/”或“*”前面的数字），然后根据pre的类型，进行相应的计算
      4. 当执行完上面的操作之后，将number变成0。然后因为扫描到的字符是“*”，所以应该将pre变成“*”
   5. 如果索引到的值为“/”：
      1. 首先判断flag的正负，然后根据这个来决定number的正负，如果flag是False，在转换完成以后需要将flag变成True
      2. 如果前面不存在pre（例如5/1），那么直接将这个number压入栈
      3. 否则从栈中退出一个元素（是“/”或“*”前面的数字），然后根据pre的类型，进行相应的计算
      4. 当执行完上面的操作之后，将number变成0。然后因为扫描到的字符是“/”，所以应该将pre变成“/”
5. 当结束循环之后，如果字符串只为一个数，那直接返回即可，如果存在操作符，那么number此时肯定不为0，需要进行判断和计算：
   1. 方法同上面重复的计算，只不过不在需要将number变成0和pre变成None。

网上也有更加简洁方便的代码，自己比较菜，写的代码有点拖沓，请见谅：

```python
        stack = []
        flag = True  # 用来判断放入该值的数是否要取负数
        pre = None  # 用来存放乘法或除法前面保存的值加方法
        number = 0
        for i in s:
            if i == " ":
                continue
            elif i == "-":
                # -1,1-1,-2-1,2*-1,2/-1，1-1/-2,1/2-1
                # 先判断前面是否有数字存在，
                if not number:  # 没有数字
                    flag = False
                else:  # 有数字，判断前面是否有乘除
                    if not flag:
                        number = -number
                    if not pre:  # 没有乘除,有数字，则将该数字压入栈 5-1
                        stack.append(number)
                    else:  # 有数字并且有乘除 1/2-1
                        a = stack.pop()
                        if pre == "/":
                            stack.append(int(a / number))
                        else:
                            stack.append(a * number)
                        pre = None
                    number = 0
                    flag = False
            elif i == "+":
                if not flag:
                    number = -number
                    flag = True
                if not pre:  # 没有乘除,有数字，则将该数字压入栈 5+1
                    stack.append(number)
                else:  # 有数字并且有乘除 1/2+1
                    a = stack.pop()
                    if pre == "/":
                        stack.append(int(a / number))
                    else:
                        stack.append(a * number)
                    pre = None
                number = 0
            elif i == "*":  # 如果遇到乘除，直接将原来的数压入栈
                if not flag:
                    number = -number
                    flag = True
                if pre:  # 2*2*2
                    a = stack.pop()
                    if pre == "/":
                        stack.append(int(a / number))
                    else:
                        stack.append(a * number)
                else:
                    stack.append(number)
                number = 0
                pre = "*"
            elif i == "/":
                if not flag:
                    number = -number
                    flag = True
                if pre:  # 2/2/2
                    a = stack.pop()
                    if pre == "/":
                        stack.append(int(a / number))
                    else:
                        stack.append(a * number)
                else:
                    stack.append(number)
                number = 0
                pre = "/"
            else:
                number *= 10
                number += int(i)
        # 最后先判断有没有number然后判断是否有乘除法，有则继续计算，然后将值加入，没有则直接判断正负，将值压入
        if number:
            if not flag:
                number = -number
            if not pre:  # 没有乘除法
                stack.append(number)
            else:
                a = stack.pop()
                if pre == "/":
                    stack.append(int(a / number))
                else:
                    stack.append(a * number)
        return sum(stack)
```

可能会发现上面有许多许多的代码重复，可以将这些重复代码写一个新的函数封装起来，直接调用即可。

## 方法三、

&nbsp;&nbsp;&nbsp;&nbsp;第三种，利用字符串的replace和strip

具体步骤来看看吧：

1. 先将原来字符串中所有的“ ”字符串变成“”（`s.replace(" ","")`），然后接下来，你需要在所有的终止符左边和右边添加空格（方便我们后面字符串的切割）`s.replace("+"," + ")`剩余的可以自己推。这里需要注意“-”号只需要添加前面的空格即可我们认为所有的负号只是起到将后面的数字从正将其转为负。`s.replace("-"," -")`。
2. 接下来，根据split将字符串变成列表`s.split()`。上面所有代码可以整合成一行即`s = s.replace(" ", "").replace("+", " + ").replace("-", " -").replace("*", " * ").replace("/", " / ").split()`
3. 利用i获取range（len(s)）：
   1. 获取该下标的值
   2. 如果这个值为“+”，则直接将这个值变成0
   3. 如果这个值为“*”，那么获取i-1下标的值，和i+1下标的值，进行乘法运算，将值放入i+1下标，其余的两个值变成0
   4. 如果这个值为“/”，那么获取i-1下标的值，和i+1下标的值，进行除法运算，将值放入i+1下标，其余的两个值变成0
   5. 如果都不是，那就说明这个下标的值是字符串类型的整数，直接把这个数取整即可
4. 最后返回整个字符串的求和即可

```python
	s = s.replace(" ","").replace("+"," + ").replace("-"," -").replace("*"," * ").replace("/"," / ").split()
        for i in range(len(s)):
            num = s[i]
            if num == "+":
                s[i] = 0
            elif num == "*":
                s[i+1] = s[i-1] * int(s[i+1])
                s[i-1],s[i] = 0,0
            elif num == "/":
                s[i+1] = int(s[i-1] / int(s[i+1]))
                s[i - 1], s[i] = 0, 0
            else:
                s[i] = int(num)
        return sum(s)
```

以上就是自己整理的关于该题的一些python解法。