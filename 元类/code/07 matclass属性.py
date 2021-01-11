# -*- coding: utf-8 -*-
# @Author  : summer

class Foo(object):
    __metaclass__ = None
    

# Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
# 如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
# 如果Python在任何父类中都找不到__metaclass_，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。



