# 如何利用ajax往后台传送json数据

后端框架：django，前端：jquery，ajax

我们在平常开发的时候会遇到：如果使用表单默认的传送方式，后台就只能从request的body获取到byte值，而python需要用字典时就有些无力，因此我们就可以使用ajax往后台传送json，再利用json库转化即可：

**方法**

ajax代码：

```javascript
// 提前构建一个字典类型的数据
let SdataParams = {
    "password": sPassword,
    "password_repeat": sPasswordRepeat,
    "mobile": sMobile,
    "sms_code": sSmsCode
};

// send ajax
$.ajax({
    url: "/user/findpwd/",  // 设置路由
    type:"POST",  // 设置请求方式
    data: JSON.stringify(SdataParams),  // 设置内容数据
    // 请求内容的数据类型（前端发给后端的格式）
    contentType: "application/json; charset=utf-8",
    dataType: "json",  // 内容数据类型
})
```

后端：

```python
def post(request):
    json_data = request.body
    data = data_dict = json.loads(json_data.decode("utf8"))
```

这样，据可以实现简单的数据传输了。