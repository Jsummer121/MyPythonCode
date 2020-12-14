import requests
import re
import pprint
number = 0
url = 'http://music.taihe.com/top/dayhot'
songsid_url = requests.get(url)
songsid_url.encoding = songsid_url.apparent_encoding
songids = re.findall('><a href="/song/(.*?)"',songsid_url.text)
for songid in songids:
	number += 1
	try:
		url_api = 'http://musicapi.taihe.com/v1/restserver/ting?' \
		'method=baidu.ting.song.playAAC&format=json&songid={}'.format(songid)
		response = requests.get(url_api).json()
		song_url = response['bitrate']['file_link']
		song_title = response['songinfo']['title']
		response = requests.get(song_url)
		with open(r'C:\users\asus\desktop\mp4\{}.mp3'.format(song_title),'wb') as f:
			f.write(response.content)
	except:
		print("第{}首下载失败....................".format(number) + song_title)
	else:
		print("正在下载第{}首....................".format(number) + song_title)
