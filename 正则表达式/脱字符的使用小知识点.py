# -*- coding: utf-8 -*-
import re

html_sock = "GET /index HTTP/1.1"

res = re.match(r"[^/]+(/[^ ]*)", html_sock)
print(res.group(1))

a = "abcd"
res = re.match(r"[^c]+", a).group()
print(res)  # "ab"  所以这里的^加上匹配单个字符表示匹配以这个结尾的之前所有元素
res = re.match(r"^a+", a).group()
print(res)  # "a"
res = re.match(r"a+", a).group()
print(res)  # "a"

