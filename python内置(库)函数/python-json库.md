# 一、json

## 1、特点

轻量级的文本数据交换格式，易与人类阅读和编写，同时也易于机器解析和生成，web世界当中最理想的数据交换格式。

## 2、前后端交互

在前段用js文件储存传输过程中用json类型进行传送，到后端，由相应的文件类型接受，python中是字典。

## 3、json语法规则

##### 1.数据由键值对组成

##### 2.键值对由逗号分隔

##### 3.大括号里保存对象

##### 4.中括号里保存数组

## 4、注意事项

##### 1.字符串必须用双引号（“”）来包括

##### 2.值可以是字符串、数字、true、false、null、列表或字典。

 ## 5、python字典转字符串

```python
json.dumps()
json.dumps(,indent=2)#控制缩进
json.dumps(,ensure_ascii=Flase)#是否使用ASCII码解析
```

json文件在python里是json格式的字符串

python里面的元组和数组在json里面直接变为数组。

中文打印出来的为Unicode字节码，要否认解析

## 6、json转python

```
json.loads()#变成字典
```

## 7、dump

将python数据转化为json，并将json保存到文件中

```
with open('json_test',"w+") as f:
	json.dump(date,indent=2,ensure_ascii=False,fp=f)#指明文件，fp=  ，这个必须写
```

## 8、load()从文件中读取json文件，并转化为python数据局

```
with open('json_test',"r+") as f:
	print(json.load(fp=f))
```

## 