# -*- coding: utf-8 -*-
import json

data = {
    "name": "菲菲",
    "age": 18,
    "feature" : ["白", "富", "美"]
}
with open('json_date','w+') as f:
    json.dump(data,indent=2,ensure_ascii=False,fp=f)

with open('json_date','r+') as f:
    res = json.load(fp=f)
    print(res["feature"][1])
