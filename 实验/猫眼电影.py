#未写完

import requests
import re
import json

def write_to_file(content):
    with open('result.txt','a')as f:
        f.write(json.dumps(content)+'\n')
        f.close()
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src"(.*?)".*?name.*?<a.*?title="(.*?)".*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*)')
    items = re.findall(pattern,html)

    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0;win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
url = 'http://maoyan.com/board/4'
req = requests.get(url,headers = headers)
html = req.text
parse_one_page(html)
for item in parse_one_page(html):
    write_to_file(item)