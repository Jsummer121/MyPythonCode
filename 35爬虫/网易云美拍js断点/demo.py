# -*- coding: utf-8 -*-
import re
url = 'https://weibo.cn/5187664653?page=2'
user_id = re.findall(r'https://weibo.cn/(\d+)?',url)[0]
print(user_id)