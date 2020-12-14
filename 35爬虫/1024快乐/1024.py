# -*- coding: utf-8 -*-
import requests
import re
import os

index = """
                             ——————————
                            |珍爱生命，远离黄赌毒|
                             ——————————
""" #显示文字

print(index)



#首页网站
url = 'http://www.4t4d.com/AAtupian/AAAwz/{}.html'


#请求头部
headers = {
'Referer': 'http://www.4t4d.com/AAtupian/AAAwz/128804.html',
'Sec-Fetch-Mode': 'no-cors',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


start_page = int(input('请输入从那一页开始的爬取：（最新的为128800）'))
end_page = int(input('请输入从那一页结束：'))
if end_page < start_page:
    start_page,end_page = end_page,start_page



#循环爬取想要的图片
for page in range(start_page,end_page+1):
    print('现在爬取第{}页'.format(page))

    # 获取在网页的源代码
    data = requests.get(url.format(page),headers = headers)
    data.encoding = 'utf-8'#使用text时，进行编译的预处理，因为代码会自动检测编码格式，80%是正确的，但是还是在有些时候是错误的，需要自己进行编写

    #因为有些图片链接放在不同的地方所以需要不同的正则来拿取
    img = re.findall(r'class="zoom" src="(.*?)"',data.text,re.S)
    if not img:
        img = re.findall(r'<img src="(.*?)">',data.text,re.S)
    image_path = './images/{}'.format(page)


    #查看个个文件夹是否存在
    #查看并创建放图片的文件夹的文件夹
    if not os.path.exists('./images'):
        os.mkdir('./images')
    #查看并创建放图片的文件夹
    if not os.path.exists(image_path):
        os.mkdir(image_path)


    #根据获取的图片url链接数量来循环爬取图片
    for i in range(len(img)):
        #获取图片的数据
        img_data = requests.get(img[i],headers=headers)
        #写入
        with open('{}/{}'.format(image_path,img[i].split('/')[-1]), 'wb') as f:
            f.write(img_data.content)
