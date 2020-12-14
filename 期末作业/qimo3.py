# -*- coding: utf-8 -*-
# 3.设计一个程序，通过输入文件名，会自动创建文件，创建后提示需要写入的内容，
# 可以在里面写入文件内容，然后自动保存退出。
name = input("请输入文件名：")
name = name+'.txt'
print("已成功创建"+name+"文件夹")
a = open(name,"w+",encoding="UTF-8")
a.close() #创建相应的txt文件
text = input("请输入你想加入的内容：")
with open(name,"a+",encoding="UTF-8") as b:
    b.write(text+"\n")
