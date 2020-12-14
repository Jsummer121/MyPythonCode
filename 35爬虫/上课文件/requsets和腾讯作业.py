# import re
# import json
# import requests
#
# def parse_response(res):
#     response = res.content.decode('gbk')
#     title = re.findall(r'<span class="niae2_top">提问：(.*?)</span>',response,re.S)
#     content = re.findall(r'<td class="txt16_3" >&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</td>',response,re.S)
#     a = re.sub(r'<.*?>','',content[0])
#     number = re.findall(r'编号:(\d+)</span></td',response,re.S)
#     result = re.findall(r'网友：(.*?) 发言时间：(\d+-\d+-\d+ \d+:\d+:\d+)',response)
#
#     if not a:
#         print(res.url)
#         print(content)
#     items = {
#         '标题':title[0],
#         '内容':a,
#         '编号':number[0],
#         '网友':result[0][0],
#         '发布时间':result[0][1],
#     }
#     print(items)
#     return items
#
# def save_items(urls):
#     for url in urls:
#         detail_res = requests.get(url)
#         items = parse_response(detail_res)
#         f.write(json.dumps(items,ensure_ascii=False)+'\n\n')
#
#
# if __name__ == '__main__':
#     f = open('items.json','w',encoding='utf-8')
#     url = 'http://wz.sun0769.com/index.php/question/questionType?page={}'
#     for i in range(0,301,30):
#         res = requests.get(url.format(i)).content.decode('gbk')
#         urls = re.findall(r'</a> <a href="(.*?shtml)" ', res, re.S)
#         save_items(urls)
#     f.close()
#

import requests


url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1571491531533&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

for page in range(1,10):
    data = requests.get(url.format(page)).json()
    for i in data.get('Data').get('Posts'):
        print(i)
