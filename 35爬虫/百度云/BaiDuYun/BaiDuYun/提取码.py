# -*- coding: utf-8 -*-
from selenium import webdriver
import time
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# 打开浏览器
driver = webdriver.Chrome()
# 打开登录界面
driver.get('https://pan.baidu.com/share/init?surl=_MeZcwsgRSUW3fIor9zcug')
time.sleep(2)

# for a in l1:
for b in l1:
    for c in l1:
          for d in l1:
                password = 'a'+b+c+d
                # 定位输入框 输入提取码
                id_text = driver.find_element_by_id('jbq2mRW')  # 根据id定位到相应的点。
                id_text.clear()
                id_text.send_keys(password)
                # 定位到提交按钮
                driver.find_element_by_xpath('//a[@class="g-button g-button-blue-large"]')


# for password in passwords:
#     # 定位输入框 输入提取码
#     id_text = driver.find_element_by_id('jbq2mRW')  # 根据id定位到相应的点。
#     id_text.clear()
#     id_text.send_keys(password)
#     time.sleep(1)
#
#     # 定位到提交按钮
#     driver.find_element_by_xpath('//a[@class="g-button g-button-blue-large"]')

# 确认登录
print('提取码为:{}'.format(password))
