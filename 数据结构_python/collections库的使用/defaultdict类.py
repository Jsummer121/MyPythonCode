# -*- coding: utf-8 -*-
from collections import defaultdict

a = {}
# print(a["key"])  # KeyError

b = defaultdict(list)
print(b["key"])  # []

c = defaultdict(lambda: "NO KEY")
print(c["key"])  # NO KEY

d = defaultdict(set)  # set()
print(d["key"])

print(isinstance(d,dict))
