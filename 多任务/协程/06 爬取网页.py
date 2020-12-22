# -*- coding: utf-8 -*-
from gevent import monkey
import gevent
import urllib.request

# 有耗时操作时需要
monkey.patch_all()


def my_downLoad(url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(my_downLoad, 'http://www.baidu.com/'),
    gevent.spawn(my_downLoad, 'http://www.itcast.cn/'),
    gevent.spawn(my_downLoad, 'http://www.itheima.com/'),
])
