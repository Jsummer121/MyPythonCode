## 一、json

#### 1、特点

轻量级的文本数据交换格式，易与人类阅读和编写，同时也易于机器解析和生成，web世界当中最理想的数据交换格式。

#### 2、前后端交互

在前段用js文件储存传输过程中用json类型进行传送，到后端，由相应的文件类型接受，python中是字典。

#### 3、json语法规则

##### 1.数据由键值对组成

##### 2.键值对由逗号分隔

##### 3.大括号里保存对象

##### 4.中括号里保存数组

#### 4、注意事项

##### 1.字符串必须用双引号（“”）来包括

##### 2.值可以是字符串、数字、true、false、null、列表或字典。

 #### 5、python字典转字符串

```python
json.dumps()
json.dumps(,indent=2)#控制缩进
json.dumps(,ensure_ascii=Flase)#是否使用ASCII码解析
```

json文件在python里是json格式的字符串

python里面的元组和数组在json里面直接变为数组。

中文打印出来的为Unicode字节码，要否认解析

#### 6、json转python

```
json.loads()#变成字典
```

#### 7、dump

将python数据转化为json，并将json保存到文件中

```
with open('json_test',"w+") as f:
	json.dump(date,indent=2,ensure_ascii=False,fp=f)#指明文件，fp=  ，这个必须写
```

#### 8、load()从文件中读取json文件，并转化为python数据局

```
with open('json_test',"r+") as f:
	print(json.load(fp=f))
```

## 二、hashlib

对称加密：数据加密解密使用相同的密钥

非对称加密：加密和解密使用两把不同的密钥，公钥用于数据加密，私钥用于解密数据

单向加密（摘要算法）：只能加密数据，而不能解密数据。

#### 1、特点

##### 1.不可逆：无法根据散列值还原原来数据

##### 2.定长输出：无论输入的原始数据有多长，结果长度是相同的

##### 3.抗修改性：输入的微小改变，结果会发生巨大改变

##### 4.强碰撞性：很难找到两段内容不同的数据，使他们产生的hash值一致。几乎不可能。

#### 2、使用

```
import hashlib
#hashlib.new('md5','淘气包')#不可以，必须为二进制数进行加密，所以必须进行编码。

第一种
res = hashlib.new('md5','淘气包'.encode())#给的是对象地址。
res.digest() b'\***\'可以查看加密数据
res.hexdigset()转成16进制。

第二种
hashlib.sha256('md5','淘气包'.encode()) 

update()#先不写入值，需要时再updata一下，可以使用多次。
res = hashlib.sha1()
res.update(''.encode())
```

## 三、base64

用来将非ASCII字符的数据转化成ASCII字符的一种方法，常用于对URL的编码，可以将不打印的二进制数据转化为可打印的字符串。

```
import base64
data=''#如果字节数不够，少的字节会用等号=补全。
res = base64.b64encode(data.encode())

如果编码后的数据是用来做url或者文件路径的，那么就要选择以下方式。
res = base64.urlsafe_b64encode()
/变成_,+变成-

base64.b64decode(res)#给的是字节码
base64.b64decode(res).decode()

```

