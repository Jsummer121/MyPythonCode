import time
import pygame
import random
from mutagen.mp3 import MP3

index = """
                             ——————————
                            |无聊播放器|
                             ——————————
下面是可点播的歌曲（输入数字进行点播）
1.Bila        4.稻香          7.归程     10.有可能的夜晚      13.失夜1999
2.理想三旬    5.阴天快乐      8.马思唯   11.晚睡的姑娘        14.纠结
3.东西        6.All Stares    9.慌       12.个人简介          15.我还年轻
"""  # 显示文字
print(index)

def ply(a):
    global b, file
    if a == 1:
        file = r'..\音乐\Candy - Bila.mp3'  # 音乐路径
        b = '-Bila-'  # 歌名
    if a == 2:
        file = r'..\音乐\沈以诚 - 理想三旬（Live）.mp3'
        b = '-理想三旬-'
    if a == 3:
        file = r'..\音乐\Clever勺子 - 东西（女版）（Cover：林俊呈）.mp3'
        b = '-东西-'
    if a == 4:
        file = r'..\音乐\Hope组合 - 稻香.mp3'
        b = '-稻香-'
    if a == 5:
        file = r'..\音乐\Jeffrey - 阴天快乐.mp3'
        b = '-阴天快乐-'
    if a == 6:
        file = r'..\音乐\Fleurie - Chasing All the Stars.mp3'
        b = '-All Stares-'
    if a == 7:
        file = r'..\音乐\万花谷背锅王 - 归程.mp3'
        b = '-归程-'
    if a == 8:
        file = r'..\音乐\仙灵女巫果妹,TowC - 马思唯（MASIWEI） - 暴风雨（台灯家的果妹 ／ TowC remix）.mp3'  # 音乐路径
        b = '-马思唯-'
    if a == 9:
        file = r'..\音乐\凯瑟喵 - 谎（无念白版）.mp3'
        b = '-慌-'
    if a == 10:
        file = r'..\音乐\刘莫西 - 有可能的夜晚（Cover：曾轶可）.mp3'
        b = '-有可能的夜晚-'
    if a == 11:
        file = r'..\音乐\周新诚 - 晚睡的姑娘.mp3'
        b = '-晚睡的姑娘-'
    if a == 12:
        file = r'..\音乐\安全着陆 - 个人简介 Pt.2.mp3'
        b = '-个人简介-'
    if a == 13:
        file = r'..\音乐\安全着陆,大笑 - 失夜1999.mp3'
        b = '-失夜1999-'
    if a == 14:
        file = r'..\音乐\庆庆 - 纠结.mp3'
        b = '-纠结-'
    if a == 15:
        file = r'..\音乐\张叶蕾 - 我还年轻 我还年轻（Cover 老王乐队）.mp3'
        b = '-我还年轻-'
    return file, b

control = int(input('循环播放:1,随机播方:2,自己点播:3'))
pygame.mixer.init()  # 初始化混音器模块
while control == 1:
    for a in range(1, 16):
        file, b = ply(a)
        print('正在播放', b)
        track1 = pygame.mixer.music.load(file)  # 加载音乐文件来进行播放
        pygame.mixer.music.play()  # 开始播放
        audio = MP3(file)  # 得到音乐时长
        time.sleep(audio.info.length)  # 根据时长定时关闭
        pygame.mixer.music.stop()  # 停止播放，但不关闭窗口
while control == 2:
    a = random.randint(1, 15)
    file, b = ply(a)
    print('正在播放', b)
    track2 = pygame.mixer.music.load(file)  # 加载音乐文件来进行播放
    pygame.mixer.music.play()  # 开始播放
    audio = MP3(file)
    time.sleep(audio.info.length)  # 定时关闭
    pygame.mixer.music.stop()  # 停止播放，但不关闭窗口
while control == 3:
    a = int(input('请输入您想听得歌曲编号'))
    file, b = ply(a)
    print('正在播放', b)
    track3 = pygame.mixer.music.load(file)  # 加载音乐文件来进行播放
    pygame.mixer.music.play()  # 开始播放
    x = int(input('需要几秒后关闭这首歌？（若不需要关闭可不输入）'))
    time.sleep(x)  # 定时关闭
    pygame.mixer.music.stop()  # 停止播放，但不关闭窗口
