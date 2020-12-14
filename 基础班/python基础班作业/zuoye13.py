# -*- coding: utf-8 -*-

f = open('text.txt','w+',encoding='UTF-8')
try:
    f.write(nihao)
except Exception as e:
    print(e)
finally:
    f.close()