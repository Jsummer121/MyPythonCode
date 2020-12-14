#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/7/30 20:48

import json

# 1.将python数据转换为json：dumps（）
my_dict = {'a': 1, 'b': [1, 2, 3], 'c': (4, 5, 6), 'd': True, 'e': None}
print(type(my_dict))

res = json.dumps(my_dict)
print(res)  # {"a": 1, "b": [1, 2, 3], "c": [4, 5, 6], "d": true, "e": null}
print(type(res))    # <class 'str'>

my_dict = {'a': 1, 'd': True, 'e': None}
res = json.dumps(my_dict)
print(res)
res = json.dumps(my_dict, indent=2)
print(res)
res = json.dumps(my_dict, indent=4)
print(res)

my_dict = {'name': '小阙', 'sex': '男', 'hobby': '打篮球'}

res = json.dumps(my_dict)
print(res)  # {"name": "\u5c0f\u9619", "sex": "\u7537", "hobby": "\u6253\u7bee\u7403"}
res = json.dumps(my_dict, ensure_ascii=False)   # 是否使用ascii解析，中文字符处理
print(res)  # {"name": "小阙", "sex": "男", "hobby": "打篮球"}


# 将json转换为Python数据：loads（）
print("当前的json数据为：{}".format(res))
print(json.loads(res))  # {'name': '小阙', 'sex': '男', 'hobby': '打篮球'}
print(type(json.loads(res)))    # <class 'dict'>

# dump():将python数据转换为json并保存到文件中
# my_dict = {'a': 1, 'd': True, 'e': None}
# with open("json_test", "w+") as f:
#     json.dump(my_dict, indent=4, ensure_ascii=False, fp=f)

# load():从文件中读取json，并转换为python数据
with open("json_test", "r+")as f:
    print(json.load(fp=f))

