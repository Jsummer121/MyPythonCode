# python3.4
# json模块 传递数据
# requests url模块
# base64 编码数据
import json
import requests
import base64


#
def get_token():
    host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
    content = requests.get(host).content.decode()
    content = eval(content[:-1])
    return content['access_token']


#
def imgdata(file1path, file2path):
    with open(file1path, "rb")as f:
        pic1 = base64.b64encode(f.read())
    with open(file2path, "rb") as f:
        pic2 = base64.b64encode(f.read())

    params = json.dumps([
        {"image": str(pic1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
        {"image": str(pic2, 'utf-8'), "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"},
    ])
    return params.encode()


#
def img(file1path, file2path):
    print("开始识别 ")
    token = get_token()
    # https://aip.baidubce.com/rest/2.0/face/v3/match
    params = imgdata(file1path, file2path)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match" + "?access_token" + token
    content = requests.post(request_url, data=params).content
    content = eval(content)
    score = content['error_code']

    # score = content['result']['score']
    if score > 80:
        return "相似度" + str(score) + ",同一个人"
    else:
        return "相似度" + str(score) + ",不同一个人"


#
if __name__ == "__main__":
    print(img("图片/1.jpg", "图片/2.jpg"))

