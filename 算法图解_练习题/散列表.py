# -*- coding: utf-8 -*-

# 散列表也就是一个键值对的存储方式，即python中的字典

phoneBook = dict()
# 当然也有更加简单的方式 phoneBook = {}# 注意后面的集合也是使用{}但是使用{}来创建时，默认承认这里创建的是字典类型

phoneBook["summer"] = 1

print(phoneBook["summer"])

phoneBook["summer"] = "2"
print(phoneBook["summer"])


