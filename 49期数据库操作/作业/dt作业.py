# -*- coding: utf-8 -*-
import datetime

now = datetime.datetime.now()
res = input('请输入你的出生年月日（例如2019-01-01）：')
bir = now.strptime(res,'%Y-%m-%d')
days = now - bir
print("您出生到现在已经过去了{}天".format(days.days))
