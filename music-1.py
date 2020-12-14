# -*- coding: utf-8 -*-
import pygame
import time
import random
from mutagen.mp3 import MP3

index = """
                             ——————————
                            |    无聊播放器     |
                             ——————————
下面是可点播的歌曲（输入数字进行点播）:
1.Bila        4.稻香          7.归程     10.有可能的夜晚      13.失夜1999
2.理想三旬    5.阴天快乐      8.马思唯   11.晚睡的姑娘        14.纠结
3.东西        6.All Stares    9.慌       12.个人简介          15.我还年轻
"""
# 显示文字
print(index)
music_dic = {1: r'音乐\Candy - Bila.mp3', 2: r'音乐\沈以诚 - 理想三旬（Live）.mp3', 3: r'音乐\Clever勺子 - 东西（女版）（Cover：林俊呈）.mp3',
             4: r'音乐\Hope组合 - 稻香.mp3', 5: r'音乐\Jeffrey - 阴天快乐.mp3', 6: r'音乐\Fleurie - Chasing All the Stars.mp3',
             7: r'音乐\万花谷背锅王 - 归程.mp3', 8: r'音乐\仙灵女巫果妹,TowC - 马思唯（MASIWEI） - 暴风雨（台灯家的果妹 ／ TowC remix）.mp3',
             9: r'音乐\凯瑟喵 - 谎（无念白版）.mp3', 10: r'音乐\刘莫西 - 有可能的夜晚（Cover：曾轶可）.mp3', 11: r'音乐\周新诚 - 晚睡的姑娘.mp3',
             12: r'音乐\安全着陆 - 个人简介 Pt.2.mp3', 13: r'音乐\安全着陆,大笑 - 失夜1999.mp3', 14: r'音乐\庆庆 - 纠结.mp3',
             15: r'音乐\张叶蕾 - 我还年轻 我还年轻（Cover 老王乐队）.mp3'}

music_name = {1: '-Bila-', 2: '-理想三旬-', 3: '-东西-', 4: '-稻香-', 5: '-阴天快乐-', 6: '-All Stares-', 7: '-归程-', 8: '-马思唯-',
              9: '-慌-', 10: '-有可能的夜晚-', 11: '-晚睡的姑娘-', 12: '-个人简介-', 13: '-失夜1999-', 14: '-纠结-', 15: '-我还年轻-'}


def play_music(num):
    print('正在播放的音乐是:', music_name[num])
    pygame.mixer.init()  # 初始化混音器模块
    file = music_dic[num]
    pygame.mixer.music.load(file)  # 加载音乐文件来进行播放
    pygame.mixer.music.play()  # 开始播放
    audio = MP3(file)  # 得到音乐时长
    time.sleep(audio.info.length)  # 根据时长定时关闭
    pygame.mixer.music.stop()  # 停止播放，但不关闭窗口


control = int(input(
    '''循环播放:1,随机播方:2,自己点播:3
您的选择是：'''))
music_list = list(range(1, 16))

if control == 1:
    for num in music_list:
        play_music(num)
elif control == 2:
    while True:
        if music_list:
            num = random.randint(1, 15)
            if num in music_list:
                music_list.remove(num)
                play_music(num)
            else:
                continue
        else:
            break
else:
    while True:
        num = int(input('请输入想听的音乐:'))
        play_music(num)