# Ajax的同步与异步

现在的前端开发绝大多是的时候需要用到ajax，而用ajax势必会用到同步与异步属性（async）。

![img](https://images2017.cnblogs.com/blog/1216351/201708/1216351-20170814140456928-1664476444.png)

在jquery的ajax中如果我们希望实现同步或者异步我们可以直接设置async发生为真或假即可true false，下面是我实际开发中遇到的一个两个例子：

例1:

```javascript
sReturnValue = "";
// send sjax
$.ajax({
    url: "/mobiles/" + sMobile + "/",
    type: "GET",
    dataType: "json",
}).done(function (res) {
    if(res.data.count !== 0){
        message.showError("手机号已注册，请重新输入")
    }else{
        message.showSuccess("手机号可以正常使用");
        sReturnValue = "success"
    }
}).fail(function () {
    message.showError("服务器超时，请重试！")
});
return sReturnValue;
```

例2：

```javascript
sReturnValue = "";
// send sjax
$.ajax({
    url: "/mobiles/" + sMobile + "/",
    type: "GET",
    dataType: "json",
    async: false  //使用同步的方式,true为异步方式
}).done(function (res) {
    if(res.data.count !== 0){
        message.showError("手机号已注册，请重新输入")
    }else{
        message.showSuccess("手机号可以正常使用");
        sReturnValue = "success"
    }
}).fail(function () {
    message.showError("服务器超时，请重试！")
});
return sReturnValue;
```

在这里，在网页同时通过ajax往后台发送数据时，例2会一直在done哪里等待后台返回数据，而例1在等待server端返回的这个过程中，前台会继续 执行ajax块后面的脚本，直到server端返回正确的结果才会去执行success，也就是说这时候执行的是两个线程，ajax块发出请求后一个线程 和ajax块后面的脚本（另一个线程）

例3

```javascript
$.ajax({ 
    type:"POST",
    url:"Venue.aspx?act=init",
    dataType:"html",
    success:function1(result){   //function1()
        f1();
        f2();
    }
    failure:function1(result) { 
    alert('Failed');
})
function2();
```

在上例中，当ajax块发出请求后，他将停留function1()，等待server端的返回，但同时（在这个等待过程中），前台会去执行function2(),也就是说，在这个时候出现两个线程，我们这里暂且说为function1() 和function2()。

当把asyn设为false时，这时ajax的请求时同步的，也就是说，这个时候ajax块发出请求后，他会等待在function1（）这个地方，不会去执行function2()，知道function1()部分执行完毕。
注意

同步的意思是当JS代码加载到当前AJAX的时候会把页面里所有的代码停止加载，页面出去假死状态，当这个AJAX执行完毕后才会继续运行其他代码页面假死状态解除。

而异步则这个AJAX代码运行中的时候其他代码一样可以运行。

因此回到例1，如果我使用默认的异步，在ajax请求后台数据之后，并不会一直等待后台的数据返回，而是直接去执行主线程接下来的代码（return sReturnValue），而此时我刚好需要后台返回的数值作为我判断的条件，因此就会出现，无论我后台的返回数据是咋样的，通过这个ajax返回的数据就只是一个空。因此为了避免这样的错误，我们需要将异步设置为flase。