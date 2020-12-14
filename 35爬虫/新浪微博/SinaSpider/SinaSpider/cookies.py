# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from .user import account,password
import json
import redis

user_list=[
    (account,password)
]

def get_cookies(account,password):
    #打开浏览器
    driver = webdriver.Chrome()
    #打开登录界面
    driver.get('https://passport.weibo.cn/signin/login')
    time.sleep(2)
    #定位输入框 输入账号
    username = driver.find_element_by_id('loginName')#根据id定位到相应的点。
    username.clear()
    username.send_keys(account)

    time.sleep(2)
    #定位到密码输入框 输入密码
    psd = driver.find_element_by_id('loginPassword')
    psd.clear()
    psd.send_keys(password)

    #定位登录按钮 点击登录
    commit = driver.find_element_by_id('loginAction')
    commit.click()
    time.sleep(2)

    #定位到获取短信验证码
    note = driver.find_element_by_id('getCode')
    note.click()
    time.sleep(20)

    #定位验证按钮
    # driver.find_element_by_xpath('//span[@class="geetest_radar_tip_content"]')
    # time.sleep(10)

    # 定位到确认按钮
    driver.find_element_by_xpath('//a[@class="submit-btn m-btn m-btn-block m-btn-orange"]')

    time.sleep(10)
    # 确认登录
    print('-----登陆成功----')

    #获取cookies数据
    cookie = {}
    for item in driver.get_cookies():
        cookie[item['name']] = item['value']
    return json.dumps(cookie)

def initCookies(rconn):
    #建立和redis的连接
    # rconn = redis.Redis(host='127.0.0.1',port=6379)
    for usr in user_list:
        if rconn.get('Cookies:{}'.format(account)) is None:
            cookie = get_cookies(usr[0],usr[1])
            if len(cookie) > 0:
                rconn.set('Cookies:{}'.format(account),cookie)




