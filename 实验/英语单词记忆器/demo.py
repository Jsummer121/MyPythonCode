# -*- coding: utf-8 -*-
import random
from datetime import datetime

# 1.用于存储所有单词，存储类型：字典
total_words = {
    'abandon': ["丢弃", '离弃', '放弃'], 'abnormal': ['不正常的', '异常的'], 'abolish': ['彻底废除', '废止'],
    'abortion': ['流产', '堕胎', '失败', '夭折'], 'abrupt': ['突然地', '仓促的', '唐突的', '鲁莽的'],
    'absence': ['缺席', '不在场', '缺乏', '不存在'], 'absolute': ['绝对的', '完全的', '确实的', '专制的', '无限制的', '无条件的'],
    'abstract': ['抽象的', '摘要', '抽象', '提取', '抽取'], 'absurd': ['荒谬的', '荒唐的'],
    'abundance': ['大量', '丰富', '充足'], 'abuse': ['辱骂', '污蔑', '虐待', '滥用'],
    'accelerate': ['加快', '增速'], 'access': ['接近', '获得', '通道', '入口'],
    'accessory': ['附近', '配件', '装饰品', '同谋', '包庇犯'], 'accidental': ['意外的', '发生的'],
    'accommodate': ['容纳', '使适应', '向…提供住宿', '顺应'], 'accommodation': ['住宿', '膳食', '适应', '调节'],
    'accompany': ['陪伴', '陪同', '伴随', '为…伴奏'], 'accord': ['一致', '符合', '谅解', '授予'],
    'accordance': ['一致', '和谐', '授予', '给予'], 'accountant': ['会计师', '会计人员'],
    'accumulate': ['堆积', '积累', '积聚', '累积'], 'accuracy': ['准确性', '精确性', '正确性'],
    'accurate': ['正确的', '正确无误的', '准确的', '精确的'], 'accuse': ['指责', '指控', '控告'],
    'acknowledge': ['承认', '理会', '确认', '报答'], 'acquaint': ['使了解', '使认识', '使熟悉'],
    'acquaintance': ['认识', '相识', '了解'], 'acquisition': ['获得物', '取得', '获得', '习得'],
    'activate': ['使活动起来', '活动'], 'acute': ['严重的', '激烈的', '敏锐的', '尖的'],
    'addict': ['使成瘾', '使入迷', '有瘾的人', '入迷的人'], 'addition': ['加', '加法', '增加的人或物'],
    'additional': ['添加的', '额外的', '另外的'], 'account': ['记述', '描述', '报告', '账户', '解释', '说明']
}

# 2.获取存储在total_words里面的关键字
words = list(total_words.keys())
lens = len(words)  # 获取words的长度
wrong_word = []

# 一、单次测试
#
#
# # 3.随机产生一个0-lens-1的整数数，并获取该数在words所对应的值
# word_int = random.randint(0, lens - 1)
# word = words[word_int]
#
# # 4.将该单词输出，并且获取用户输入的该单词的意思，并进行判断
# word_in = input(word + '：单词的意思为：\n')
# if (word_in in total_words[word]):
#     # 如果用户输入的单词存在意思库里，则打印出正确
#     print("恭喜你，该题做对啦！")
# else:
#     # 否则就打印出错误
#     print("很遗憾，"+str(word)+'的意思为：'+'、'.join(total_words[word]))

# 二、多次测试（单词会重复）
# total_len = int(input('请输入需要测试的单词个数（共' + str(lens) + '个）:'))
# right = 0
# for i in range(total_len):
#     # 3.随机产生一个0-lens-1的整数数，并获取该数在words所对应的值
#     word_int = random.randint(0, lens - 1)
#     word = words[word_int]
#
#     # 4.将该单词输出，并且获取用户输入的该单词的意思，并进行判断
#     word_in = input(word + '：单词的意思为：\n')
#     if (word_in in total_words[word]):
#         # 如果用户输入的单词存在意思库里，则打印出正确
#         print("恭喜你，该题做对啦！")
#         right += 1
#     else:
#         # 否则就打印出错误
#         print("很遗憾，"+str(word)+'的意思为：'+'、'.join(total_words[word]))


# 三、多次测试（单词不会重复）
total_len = int(input('请输入需要测试的单词个数（共' + str(lens) + '个）:'))
this_time = 0  # 用来存储当前的执行次数
right = 0  # 用来记录正确题目的个数
word_list = []  # 用来存储已经出现过的单词
while (this_time != total_len):
    # 3.随机产生一个0-lens-1的整数数，并获取该数在words所对应的值
    word_int = random.randint(0, lens - 1)
    word = words[word_int]
    if (word in word_list):
        continue
    word_list.append(word)
    this_time += 1
    # 4.将该单词输出，并且获取用户输入的该单词的意思，并进行判断
    word_in = input(word + '：单词的意思为：\n')
    if (word_in in total_words[word]):
        # 如果用户输入的单词存在意思库里，则打印出正确
        print("恭喜你，该题做对啦！")
        right += 1
    else:
        # 否则就打印出错误
        print("很遗憾，" + str(word) + '的意思为：' + '、'.join(total_words[word]))
        wrong_word.append(word)

print('\r\n恭喜你，这次一共做了' + str(total_len) + '题，做对了' + str(right) + '题，正确率为：' + str(int(right / total_len * 100)) + '%')

# 如果存在错题，则将错题输出在屏幕上并且将错误的题目写入wrong.txt文件内
if total_len - right != 0:
    with open('wrong.txt', 'a+', encoding="utf-8") as f:  # 将错误的单词写入文本
        now = datetime.now()
        f.write('\n' + now.ctime() + '\n')  # 将日期时间写入文件
    print('您的错误单词一共有' + str(total_len - right) + '题，分别是：')
    for j in range(len(wrong_word)):
        str1 = wrong_word[j] + '：' + ','.join(total_words[wrong_word[j]])
        print(str1)
        with open('wrong.txt', 'a+', encoding="utf-8") as f:  # 将错误的单词写入文本
            f.write(str(str1 + '\n'))
