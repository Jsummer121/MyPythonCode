## URL的编解码

在平常使用url的时候，我们复制一个网页到另一个地方会发现编码是乱的，此时再去浏览这个网页就会发现还是可以出来的。

其实这只是一个正常的现象，我们从浏览器输入网址，然后这个url经过编码发送给服务器，服务器再转发给我们的框架，框架将值存放如mysql，所以此时如果是按值放入的是经过编码的url值，要想获得正确的值必须解码。python3下可以使用``urllib.parse`函数

```python
>>> import urllib.parse
>>> print(urllib.parse.quote("summer"))
summer
>>> print(urllib.parse.quote("哈哈哈哈"))
%E5%93%88%E5%93%88%E5%93%88%E5%93%88
>>> print(urllib.parse.unquote("%E5%93%88%E5%93%88%E5%93%88%E5%93%88"))
哈哈哈哈
```

因此，只需要经这个函数解码即可获得原来的值了。