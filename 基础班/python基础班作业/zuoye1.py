#1.定义讲过的每种数字类型并实现相互之间的转换
#整数类型 int
a = 3
#浮点型 float
b = 1.3
#复数 complex
c = 2+3j

print('a的类型'+str(type(a))+'b的类型'+str(type(b))+'c的类型'+str(type(c)))

a1 = int(b)
b1 = float(a)

print('a1的类型'+str(type(a1))+'b1的类型'+str(type(b1)))

#2有一个时间形式(eg: 20191202),要求从这个格式中得到年、月、日
eg = '20191202'
print(eg+'表示：'+eg[:4]+'年'+eg[4:6]+'月'+eg[6:]+'日')