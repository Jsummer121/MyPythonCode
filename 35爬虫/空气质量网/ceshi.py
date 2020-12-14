# -*- coding: utf-8 -*-
import execjs
import nodejs

#1
# print(execjs.get())
#2
# print(execjs.eval('"red blue".split(" ")'))
#3 加载js代码
ctx = execjs.compile("""
    function add(x,y){
        return x+y;
    }
""")


print(ctx.call("add","1","2"))
# js = 'add{}'
