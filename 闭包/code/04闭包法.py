# -*- coding: utf-8 -*-
# @Author  : summer


def test(k, b):
	def create(x):
		print(k * x + b)
	return create


t = test(1, 2)
t(1)
