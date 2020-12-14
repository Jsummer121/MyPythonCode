# -*- coding: utf-8 -*-
import re
url = "www.baidu.com"
head = re.findall("^www",url)
last = re.findall("com$",url)
s1 = ''.join(head)
s2 = ''.join(last)
s = s1+'.'+"baidu"+'.'+s2
print(s)