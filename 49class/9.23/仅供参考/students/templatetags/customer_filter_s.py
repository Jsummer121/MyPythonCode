#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:fei time:2019/9/18 21:05
from django import template

register = template.Library()


@register.filter()
def to_male(value, flag="zh"):
    change = {
        "zh": ("女", "男"),
        "en": ("Female", "Male"),
    }
    return change[flag][value]
