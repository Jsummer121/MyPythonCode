import base64
import json
import  requests
#1。读取图片数据 整合两站照片数据
with open("图片/1.jpg","rb") as f:
    pic1 = base64.b16encode(f.read())

with open("图片/2.jpg","rb") as f:
    pic2 = base64.b16encode(f.read())

image_data = json.dumps([
      {"image":str(pic1,'utf-8'), "image_type": "BASE64","face_type": "LIVE", "quality_control": "LOW"},
      {"image":str(pic2,'utf-8'), "image_type": "BASE64","face_type": "IDCARD", "quality_control": "LOW"},
  ])
#2.拼接api
get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
API_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="

text = requests.get(get_token)
access_token = json.loads(text.text)['access_token']
url = API_url + access_token
#3.请求api接口传入图片数据，返回图片相似度
response = requests.post(url,image_data)
score = json.loads(response.text)['result']['score']
if score > 80:
    print('图片相似度为：' + score + '是同一个人')
else:
    print('图片相似度为：' + score + '不是同一个人')