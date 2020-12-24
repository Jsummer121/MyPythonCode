# -*- coding: utf-8 -*-
import re

emails = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com", "com.xiaowang@qq.com", "xiaowang@qq.com.com", "summer@icloud.com"]

for email in emails:
    res = re.match(r"[\w]{4,20}@(163|qq|icloud).com$", email)
    if res:
        print("%s 是规范的邮箱" % email)
    else:
        print("%s 不是规范的邮箱" % email)
