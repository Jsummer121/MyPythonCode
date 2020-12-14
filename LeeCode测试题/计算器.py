# -*- coding: utf-8 -*-


def calculate(s):
    # 正规解法
    # 1.创建一个栈
    # 2.依次取值，
    # 3.将栈内的所有元素相加即是答案
    # stack = []
    # flag = True  # 用来判断放入该值的数是否要取负数
    # pre = None  # 用来存放乘法或除法前面保存的值加方法
    # number = 0
    # for i in s:
    #     if i == " ":
    #         continue
    #     elif i == "-":
    #         # -1,1-1,-2-1,2*-1,2/-1，1-1/-2,1/2-1
    #         # 先判断前面是否有数字存在，
    #         if not number:  # 没有数字
    #             flag = False
    #         else:  # 有数字，判断前面是否有乘除
    #             if not flag:
    #                 number = -number
    #             if not pre:  # 没有乘除,有数字，则将该数字压入栈 5-1
    #                 stack.append(number)
    #             else:  # 有数字并且有乘除 1/2-1
    #                 a = stack.pop()
    #                 if pre == "/":
    #                     stack.append(int(a / number))
    #                 else:
    #                     stack.append(a * number)
    #                 pre = None
    #             number = 0
    #             flag = False
    #     elif i == "+":
    #         if not flag:
    #             number = -number
    #             flag = True
    #         if not pre:  # 没有乘除,有数字，则将该数字压入栈 5-1
    #             stack.append(number)
    #         else:  # 有数字并且有乘除 1/2+1
    #             a = stack.pop()
    #             if pre == "/":
    #                 stack.append(int(a / number))
    #             else:
    #                 stack.append(a * number)
    #             pre = None
    #         number = 0
    #     elif i == "*":  # 换思路，如果遇到乘除，直接将原来的数压入栈
    #         if not flag:
    #             number = -number
    #             flag = True
    #         if pre:  # 2*2*2
    #             a = stack.pop()
    #             if pre == "/":
    #                 stack.append(int(a / number))
    #             else:
    #                 stack.append(a * number)
    #         else:
    #             stack.append(number)
    #         number = 0
    #         pre = "*"
    #     elif i == "/":
    #         if not flag:
    #             number = -number
    #             flag = True
    #         if pre:  # 2/2/2
    #             a = stack.pop()
    #             if pre == "/":
    #                 stack.append(int(a / number))
    #             else:
    #                 stack.append(a * number)
    #         else:
    #             stack.append(number)
    #         number = 0
    #         pre = "/"
    #     else:
    #         number *= 10
    #         number += int(i)
    # # 最后先判断有没有number然后判断是否有乘除法，有则继续计算，然后将值加入，没有则直接判断正负，将值压入
    # if number:
    #     if not flag:
    #         number = -number
    #     if not pre:  # 没有乘除法
    #         stack.append(number)
    #     else:
    #         a = stack.pop()
    #         if pre == "/":
    #             stack.append(int(a / number))
    #         else:
    #             stack.append(a * number)
    # return sum(stack)
    s = s.replace(" ", "").replace("+", " + ").replace("-", " -").replace("*", " * ").replace("/", " / ").split()
    for i in range(len(s)):
        num = s[i]
        if num == "+":
            s[i] = 0
        elif num == "*":
            s[i + 1] = s[i - 1] * int(s[i + 1])
            s[i - 1], s[i] = 0, 0
        elif num == "/":
            s[i + 1] = int(s[i - 1] / int(s[i + 1]))
            s[i - 1], s[i] = 0, 0
        else:
            s[i] = int(num)
    return sum(s)


if __name__ == '__main__':
    while True:
        print(calculate(input()))
