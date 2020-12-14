# -*- coding: utf-8 -*-
import requests


url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1571710017415&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
for page in range(1,3):
    data = requests.get(url.format(page),verify=False).json()
    for detail_data in data.get('Data').get('Posts'):
        PostId = detail_data.get('PostId')
        RecruitPostName = detail_data.get('RecruitPostName')
        CountryName = detail_data.get('CountryName')
        LocationName = detail_data.get('LocationName')
        Responsibility = detail_data.get('Responsibility')
        print('ID:{}\n招聘名称：{}\n国家：{}\n地区：{}\n方向：{}'.format(PostId,RecruitPostName,CountryName,LocationName,Responsibility))
