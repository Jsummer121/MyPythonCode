# -*- coding: utf-8 -*-
import requests
ee = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-10-21&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=TJP&purpose_codes=ADULT',verify=False)
print(ee.content)