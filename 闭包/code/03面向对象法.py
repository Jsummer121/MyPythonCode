# -*- coding: utf-8 -*-
# @Author  : summer

class Create:
	def __init__(self, k, b):
		self.k = k
		self.b = b
	
	def __call__(self, x, *args, **kwargs):
		print(self.k * x + self.b)


c1 = Create(1, 2)
c1(1)
