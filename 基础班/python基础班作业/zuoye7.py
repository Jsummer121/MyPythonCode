# 定义一个函数，能够输入字典和元组。函数返回一个字典和元组，字典的value值和元组的值交换

# 变量初始化
tu = ('fei', 18, 160)
di = {'name': 'sophia', 'age': 20, 'height': 165}

# 函数式编程
def func(tu, di):
    return dict(zip(di.keys(), tu)), tuple(di.values())

x, y = func(tu, di)
print(x)
print(y)


