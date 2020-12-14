# jieba



## cut

有两个参数

1.是带分的字符串

2.cut_all 用来控制是否采用全模式



### 1.全模式

```python
all_list = jieba.cut('今天天气真好，亲爱的，我们去远足吧！',cut_all=True)
>>> print(all_list)
>>> <generator object Tokenizer.cut at 0x02940A70>
>>> print('|'.join(all_list))
>>> 今天|今天天气|天天|天气|真好|||亲爱|的|||我们|去|远足|吧||
```

### 精确模式（默认模式）

```python
mak_list = jieba.cut('今天天气真好，亲爱的，我们去远足吧！',cut_all=False)
>>> print('|'.join(mak_list))
>>> 今天天气|真|好|，|亲爱|的|，|我们|去|远足|吧|！
```

### 搜索引擎模式

```
sea_list = jieba.cut_for_search('今天天气真好，亲爱的，我们去远足吧！')
>>> print('|'.join(sea_llist))
>>> 今天|天天|天气|今天天气|真|好|，|亲爱|的|，|我们|去|远足|吧|！
```

## TF-IDF

是一种信息检索与数据挖掘的常用加权技术

TF是词频，之关键词在文中出现的次数除以全文总字数

IDF是指逆文本评率指数(如的，得，地),反映关键词的普遍程度，当一个词越普遍时，		IDF值越低反之IDF值越高。

**可以看出：**

当一个词在文档频率越高并且新鲜度越高，其TF-IDF越高

TF-IDF兼顾词频与新鲜度，过滤一些常用词，能保留更多信息的重要词



基于TF-IDF算法的关键词抽取：

```
import jieba.analyse
jieba.analyse.extract_tags(sentence,topK=20,withWeight=False,allowPOS=())
```

sentence:待提取文本

topK:返回几个TF/IDF权重最大的关几词，默认为20

withWeight:是否一并返回关键词权重值，默认为False

allowPOS:词性过滤，为空表示不过滤，若提供则仅返回复合词性要求的关键词

#### 附：结巴分词词性对照表（按词性英文首字母排序）

###### 形容词(1个一类，4个二类)

- a 形容词
- ad 副形词
- an 名形词
- ag 形容词性语素
- al 形容词性惯用语

###### 区别词(1个一类，2个二类)

- b 区别词
- bl 区别词性惯用语

###### 连词(1个一类，1个二类)

- c 连词
- cc 并列连词

###### 副词(1个一类)

- d 副词

###### 叹词(1个一类)

- e 叹词

###### 方位词(1个一类)

- f 方位词

###### 前缀(1个一类)

- h 前缀

###### 后缀(1个一类)

- k 后缀

###### 数词(1个一类，1个二类)

- m 数词
- mq 数量词

###### 名词 (1个一类，7个二类，5个三类)

*名词分为以下子类：*

- **n 名词**
- **nr 人名**
- nr1 汉语姓氏
- nr2 汉语名字
- nrj 日语人名
- nrf 音译人名
- **ns 地名**
- nsf 音译地名
- **nt 机构团体名**
- **nz 其它专名**
- **nl 名词性惯用语**
- **ng 名词性语素**

###### 拟声词(1个一类)

- o 拟声词

###### 介词(1个一类，2个二类)

- p 介词
- pba 介词“把”
- pbei 介词“被”

###### 量词(1个一类，2个二类)

- q 量词
- qv 动量词
- qt 时量词

###### 代词(1个一类，4个二类，6个三类)

- **r 代词**
- **rr 人称代词**
- **rz 指示代词**
- rzt 时间指示代词
- rzs 处所指示代词
- rzv 谓词性指示代词
- **ry 疑问代词**
- ryt 时间疑问代词
- rys 处所疑问代词
- ryv 谓词性疑问代词
- **rg 代词性语素**

###### 处所词(1个一类)

- s 处所词

###### 时间词(1个一类，1个二类)

- t 时间词
- tg 时间词性语素

###### 助词(1个一类，15个二类)

- u 助词
- uzhe 着
- ule 了 喽
- uguo 过
- ude1 的 底
- ude2 地
- ude3 得
- usuo 所
- udeng 等 等等 云云
- uyy 一样 一般 似的 般
- udh 的话
- uls 来讲 来说 而言 说来
- uzhi 之
- ulian 连 （“连小学生都会”）

###### 动词(1个一类，9个二类)

- v 动词
- vd 副动词
- vn 名动词
- vshi 动词“是”
- vyou 动词“有”
- vf 趋向动词
- vx 形式动词
- vi 不及物动词（内动词）
- vl 动词性惯用语
- vg 动词性语素

###### 标点符号(1个一类，16个二类)

- w 标点符号
- wkz 左括号，全角：（ 〔 ［ ｛ 《 【 〖 〈 半角：( [ { <
- wky 右括号，全角：） 〕 ］ ｝ 》 】 〗 〉 半角： ) ] { >
- wyz 左引号，全角：“ ‘ 『
- wyy 右引号，全角：” ’ 』
- wj 句号，全角：。
- ww 问号，全角：？ 半角：?
- wt 叹号，全角：！ 半角：!
- wd 逗号，全角：， 半角：,
- wf 分号，全角：； 半角： ;
- wn 顿号，全角：、
- wm 冒号，全角：： 半角： :
- ws 省略号，全角：…… …
- wp 破折号，全角：—— －－ ——－ 半角：--- ----
- wb 百分号千分号，全角：％ ‰ 半角：%
- wh 单位符号，全角：￥ ＄ ￡ ° ℃ 半角：$

###### 字符串(1个一类，2个二类)

- x 字符串
- xx 非语素字
- xu 网址URL

###### 语气词(1个一类)

- y 语气词(delete yg)

###### 状态词(1个一类)

- z 状态词

```
import jieba.analyse

f = open('123.txt','rb')
sentence = f.read()

keyword == jieba.analyse.extract_tags(sentence,topK=15,withWeight=True,allowPOS=('n','ns','nr'))

for item in wkewords:
	print(item[0],item[1])
```

#### 实战 统计三国演义小说词频钱20的词

```
import jieba
f = open('sanguo.txt','rb')
txt = f.read()
words = jieba.lcut(txt)
counts = {}

for word in words:
	if len(word) == 1:
		contioue
	else:
		counts[word] = counts.get(word,0)+1
		
items = list(counts.items())
items.sort(key = lambda items: items[1],reverse = True)
for i in range(20):
	word,count = items[i]
	print("{0<10}{1:5}".format(word,count))
```

