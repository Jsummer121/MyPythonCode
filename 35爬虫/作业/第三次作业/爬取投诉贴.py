# -*- coding: utf-8 -*-

import re
import requests
import json

url = 'http://wz.sun0769.com/index.php/question/questionType?type=4'

res = requests.get(url)
res.encoding = 'gbk'
# print(res.text)

#获取id
qu_id = re.findall(r'<td width="53" height="30" align="center" bgcolor="#FFFFFF">(.*?)</td>',res.text,re.S)
#获取url和name
qu_url_names = re.findall(r'</a> <a href="(.*?)" title="(.*?)"',res.text,re.S)

num  = 0
for qu_url_name in qu_url_names:
    res_detail = requests.get(qu_url_name[0])
    res_detail.encoding = 'gbk'
    detail = re.findall(r'<meta name="description" content="(.*?)" />',res_detail.text,re.S)
    if 'div' in detail[0]:
        detail = re.findall(r"<div class='contentext'>(.*?)<",detail[0],re.S)
    dict = {'id':qu_id[num],'url':qu_url_name[0],'title':qu_url_name[1],'content':detail}
    num +=  num
    js = json.dumps(dict,ensure_ascii=False)
    print(js)

