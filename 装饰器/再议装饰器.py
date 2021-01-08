# -*- coding: utf-8 -*-
# @Author  : summer

# 定义函数：完成包裹数据
def makeBold(fn):
	print("makeBold")
	
	def wrapped():
		return "<b>" + fn() + "</b>"
	
	return wrapped


# 定义函数：完成包裹数据
def makeItalic(fn):
	print("makeItalic")
	
	def wrapped():
		return "<i>" + fn() + "</i>"
	
	return wrapped


@makeBold
def test1():
	return "hello world-1"


@makeItalic
def test2():
	return "hello world-2"


@makeBold
@makeItalic
def test3():
	return "hello world-3"


print(test1())
print("-"*20)
print(test2())
print("-"*20)
print(test3())
