#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/9/7 21:14
from django import template


register = template.Library()   # 变量名必须是register


# @register.filter(name="sex1")
@register.filter()
def to_sex(value, flag='zh'):
    change = {
        'zh': ('女', '男'),
        'en': ('Female', 'Male'),
    }
    return change[flag][value]


# register.filter("sex1", to_sex)
# register.filter(to_sex)
