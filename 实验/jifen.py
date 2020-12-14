# equation：储存输入的值；a：n次方的值；b1：类型为x**n的方程;c1：类型为x**n的方程的值
import math
c1=0
equation=input('请输入需要基本积分的方程：注！：常数变量为n，变量设为x，y或z,并且不能出现分数:')
if equation[:3]=='x**'or equation[:3]=='y**'or equation[:3]=='z**':
    a=float(equation[3:])
    print('您所求的积分为'+'1/'+str(a+1)+'*'+equation[0]+'**'+str(a+1))
    bian=float(input('请输入变量的'+equation[0]+'值:'))
    def b1(bian):
        c1=1/(a+1)*bian**(a+1)
        return c1
    c1=b1(bian)
    print('您所求值为：'+str(c1))
if equation=='1/x'or equation=='1/y' or equation=='1/z':
    print('您所求的积分为'+'ln'+'|'+equation[-1]+'|')
    bian=float(input('请输入变量的'+equation[-1]+'值:'))
    c2=math.log(math.fabs(bian))
    print('您所求值为：'+str(c2))
if equation=='1/(1+x**2)' or equation=='1/(1+y**2)' or equation=='1/(1+z**2)':
    print('您所求的积分为'+'arctan'+' '+equation[-5])
    bian=float(input('请输入变量的'+equation[-5]+'值:'))
    c3=math.atan(bian)
    print('您所求值为：'+str(c3))
if equation=='1/math.sqrt(1-x**2)' or equation=='1/math.sqrt(1-y**2)' or equation=='1/math.sqrt(1-z**2)':
    print('您所求的积分为：'+'arcsin'+' '+equation[-5])
    bian=float(input('请输入变量的'+equation[-5]+'值:'))
    c4=math.asin(bian)
    print('您所求值为：'+str(c4))
if equation=='1/(1-x**2)**0.5' or equation=='1/(1-y**2)**0.5' or equation=='1/(1-z**2)**0.5':
    print('您所求的积分为：'+'arcsin'+' '+equation[-10])
    bian=float(input('请输入变量的'+equation[-10]+'值:'))
    c4=math.asin(bian)
    print('您所求值为：'+str(c4))
if equation=='sin x' or equation=='sin y' or equation=='sin z':
    print('您所求的积分为：'+'-'+'cos'+' '+equation[-1])
    bian=float(input('请输入变量的'+equation[-1]+'值:'))
    c5=-math.cos(bian)
    print('您所求值为：'+str(c5))
if equation=='cos x' or equation=='cos y' or equation=='cos z':
    print('您所求的积分为：'+'sin'+' '+equation[-1])
    bian=float(input('请输入变量的'+equation[-1]+'值:'))
    c5=-math.sin(bian)
    print('您所求值为：'+str(c5))
if equation=='1/(cos x)**2' or equation=='1/(cos y)**2' or equation=='1/(cos z)**2' or equation=='(sec x)**2' or equation=='(sec y)**2' or equation=='(sec z)**2':
    print('您所求的积分为：'+'tan'+' '+equation[-5])
    bian=float(input('请输入变量的'+equation[-5]+'值:'))
    c6=math.tan(bian)
    print('您所求值为：'+str(c6))
if equation=='1/(sin x)**2' or equation=='1/(sin y)**2' or equation=='1/(sin z)**2' or equation=='(csc x)**2' or equation=='(csc y)**2' or equation=='(csc z)**2':
    print('您所求的积分为：'+'-'+'cot'+' '+equation[-5])
    bian=float(input('请输入变量的'+equation[-5]+'值:'))
    c7=-1/math.tan(bian)
    print('您所求值为：'+str(c7))
