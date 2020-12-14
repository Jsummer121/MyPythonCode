# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#打开浏览器
option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)

#打开指定的页面
driver.get('https:www.baidu.com')