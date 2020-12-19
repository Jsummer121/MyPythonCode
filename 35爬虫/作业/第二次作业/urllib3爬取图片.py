import os
import re
import time
import urllib3
from threading import Thread



def image_request(url,item,image_path):
    # 对图片进行请求
    print('正在请求{}'.format(url))
    image_content = req.request('GET', url)  # 网络io请求
    # 文件写入图片
    print('开始写入图片')
    with open('{}/{}'.format(image_path, item[0].split('/')[-1]), 'wb') as f:
        f.write(image_content.data)


def save_images(items):
    t_list = []
    for item in items:
        if not item[0]:
            continue
        # 构造图片存储路径
        image_path = './images/{}'.format(item[1])
        # 判断文件夹是否存在，不存在就创建
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        # 判断图片url地址是否包含域名
        image_url = item[0]
        if not 'http' in item[0]:
            image_url = '{}{}'.format('http://www.weimeitupian.com',item[0])

        # 创建线程实例
        t = Thread(target=image_request,args=(image_url,item,image_path))
        # 启动线程
        # # 单线程
        t.start()
        t.join()
        # #多任务
    #     t_list.append(t)
    #
    # for t in t_list:
    #     t.start()
    # for t in t_list:
    #     t.join()


if __name__ == '__main__':
    req = urllib3.PoolManager()
    start_time = time.time()
    for page in range(1,4):
        print('正在下载第{}页的图片数据...'.format(page))
        data = req.request('GET','http://www.weimeitupian.com/page/{}'.format(page))
        # 通过正则表达式 匹配标题和图片地址
        items = re.findall(r'</a></div>-->.*?<img src="(.*?)" alt="(.*?)" class="thumb" />',data.data.decode(),re.S)
        save_images(items)
    print('耗时:{}秒'.format(time.time()-start_time))