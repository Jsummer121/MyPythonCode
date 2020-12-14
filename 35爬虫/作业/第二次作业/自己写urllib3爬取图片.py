# -*- coding: utf-8 -*-
import urllib3
import os
import re

def save_images(items):
    for item in items:
        if not item:
            continue
        #构造图片存储路径
        image_path= './images/{}'.format(item[1])
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        #判断图片url是否有http
        image_url = item[0]
        if not 'http' in item[0]:
            image_url = '{}{}'.format('http://www.weimeitupian.com',item[0])
        #对图片进行请求
        image_content = req.request('GET',image_url)#urllib3
        # image_content = urllib.request.urlopen(image_url)#urllib
        #文件写入图片,因为有些图片不存在权限，所以可以用try将整个过程筛选
        try:
            with open('{}/{}'.format(image_path,item[0].split('/')[-1]),'wb') as f:
                f.write(image_content.data)#urllib3
                # f.write(image_content.read())#urllib
        except:
            continue


if __name__ == '__main__':
    #实例
    req = urllib3.PoolManager()
    for page in range(1,4):
        data = req.request('get','http://www.weimeitupian.com/page/{}'.format(page))#urllib3
        # data = urllib.request.urlopen('http://www.weimeitupian.com/page/{}'.format(page)).read()#urllib
        #通过正则表达式来匹配url和图片名字
        items = re.findall(r'</a></div>-->.*?<img src="(.*?)" alt="(.*?)" class="thumb" /></a></div>',data.data.decode(),re.S)
        save_images(items)

