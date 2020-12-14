from re import sub # 用来删除邮件的标点符号等其他无关的字符
from collections import Counter # 计算邮件中出现最多的词
from itertools import chain # 可以一次返回迭代对象
from numpy import array
from jieba import cut
from sklearn.naive_bayes import MultinomialNB

def getWoedsFromFile(txtFile):
    words = []
    with open(txtFile,encoding='utf8') as fp:
        for line in fp:
            line = line.strip()
            line = sub(r'[.【】 0-9\—。、！~\*]','',line)
            line = cut(line)
            line = filter(lambda word:len(word)>1,line)
            words.extend(line)
    return words

# 获取全部训练集中出现次数最多的词
allWoeds = []
def getTopNWords(topN):
    txtFiles = [str(i)+'.txt' for i in range(151)]
    for txtFile in txtFiles:
        allWords.append(getWoedsFromFile(txtFile))
    freq = Counter(chain(*allWords))
    return [w[0] for w in freq.most_common(topN)]

topWords = getTopWoeds(600)


# 获取特征向量，创建模型训练
vectors = []
for word in allWords:
    temp = list(map(lambda x:words.count(x),topWords))
vectors = array(vectors)
labels = array([1]*127 + [0]*24)

model = MultinomialNB()
model.fit(vectors,labels)

def predict(txtFile):
    words = getWoedsFromFile(txtFile)
    currentVector = array(tuple(map(lambda x: words.count(x),topWords)))
    result = model.predict(currentVector.reshape(1,-1))[0]
    return '垃圾邮件' if result == 1 else '正常邮件'

for mail in ('%d.txt'%i for i in range(151,156)):
    print(mail,predict(mail),sep=':')
    
