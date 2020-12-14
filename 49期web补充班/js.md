# javascript

脚本语言

作用：

1.页面特效

2.前后脚虎

3.后台开发

## 一、js的使用

### 1.js的书写位置

·script标签

·常用调试方法

```
调试工具:
python里是:print
js里面是:
1.alert('ok')[这个代码他会弹出一个小框，显示ok]
2.console.log("ok")
[这个代码它实现的是在开发者工具里的console栏里打印出ok]
```

·外部文件

```
先创建一个js文件
然后在head里导入
<script src='test.js'></script>
```

### 2.js代码在html文件里的存放位置

**·HTML的head中**

如果一定要加载head里面必须在函数前面加一个window.onload = func表示窗口加载完毕才能执行代码

```
	<script>
        // alert("ok")
        // console.log("ok")
        window.onload = function (){
            var box = document.querySelector(".box");
            box.innerText = "老师你好"
        }
    </script>
```

**·HTML的body结束标签之前（推荐）**

因为代码是从上往下读取的，此时如果放前面的话，一些js他不会显示出来，所以得放后面。

### 3.注意事项

**·严格区分大小写**

**·每一行完整的语句后面加分号**

**·变量名不能使用关键字和保留字**

**·代码缩进，保持连续性**

### 4.js获取元素

```
css里面通过选择器
js里面：
1.通过标签名获取事务
var obj=document.getElementsByTagName("div");
如果HTML里面有多个div那他就获得多个
可以再('div')后面添加[0]-通过下标来获取
2.通过class名来获取事务
var obj1 = document.getElementsByClassName("box");
同样class可能出现多个，可以通过下标索引来查找
3.通过id类获得事务
var obj2 = document.getElementById("box1");
4.对于input框，可以使用上诉方法，也可以使用name来获得
var obj3 = document.getElementsByName("usr");
如果要拿到到对象，则需要加上下标
var obj3 = document.getElementsByName("usr")[0];
```

**虽然有上诉几种方法，但我们一般通过css选择器来获取对象**

```
// 通过css选择器来获取对象
灵活性更强：通用css的各种选择器
obj = document.querySelector()
如果有多个元素，但是他只找第一个元素

var obj4 = document.querySelector('div');
var obj5 = document.querySelector('.box');
var obj6 = document.querySelector("#box1");

如果需要拿到全部的元素只需要加一个all
var obj7 = document.querySelectorAll('div');
```

### 二、简单事件

**以前：**

```
<div onclick="test();">点击事情</div>
<script>
	函数定义
    function test(){
    	console.log("我是点击事件");
    }
</script>
```

**现在：**

```
<div>点击事情</div>

<script>
		#单击事件
        var box = document.querySelector("div");
        box.onclick = function () {
            console.log("单击");
        };
        #双击事件
        box.ondblclick = function () {
            console.log("双击");
        };
        #鼠标事件
        小驼峰命名法：第一个字母小写后面没一个开头字母大写
        box.onmouseenter = function () {
            box.style.backgroundColor="pink";
        };
        box.onmouseleave = function () {
            box.style.backgroundColor="skyblue";
        };
</script>
```

```
	    <select name="addr" id="">
 	        <option value="yy">岳阳</option>
  	      	<option value="wh">武汉</option>
    	    <option value="cs">长沙</option>
    	</select>
    
        #当下拉列表框发生改变
        var sel = document.querySelector("select");
        sel.onchange=function () {
            console.log("内容改变了");
        };
        #窗口发生改变
        window.onresize = function () {
            console.log("窗口变化了");
        }
```

## 三、修改样式

```
    <div class="box">我就是我，我很好，我很棒</div>
    <script>
        var obj = document.querySelector(".box");
        // 单个样式修改
        obj.style.color = "red";
        //如果不知道修改说明，需要传参的话，用[]
        var a = "background";
        var b = "blue";
        obj.style[a] = b;
        // obj.style["background"] = "blue"
        // 多个样式修改
        obj.style.cssText = "width:200px; height:200px;background:skyblue;";
        obj.style.cssText =  a+":"+b+";";//字符串拼接
        // 属性操作
    </script>
```

## 四、属性操作

属性：标签里面除了标签名和尖括号，其他都是属性

```
真实场景下操作：
<style>
        .box{
            height:200px;
            width:200px;
            background: skyblue;
        }
        .test{
            height:400px;
            width:400px;
            background: antiquewhite;
            color:peru;
        }
    </style>


<div class="box">属性操作</div>
    <script>
        // 获取元素
        var box = document.querySelector(".box");
        //js操作标签属性（增删改查）
        // 1.合法属性
        // 增
        // box.className = "box";
        // 删
        // box.removeAttribute("class");
        //此时class属性被删除
        // 改
        // box.className="test";
        // 查（获取）
        // console.log(box.className)
        
        // 2.自定义属性
        // 增
        box.setAttribute("hh", "ww");
        // 改
        box.setAttribute("hh", "tt");
        // 查(判断）
        console.log(box.hasAttribute("hh"));
        //	true或者False
        // 删
        box.removeAttribute("hh");
    </script>
```

## 五、数据类型

六大数据类型

1.Numer类型：整数，小数

注意：NaN:not a number。也是数字类型

isNaN(用来检查一个参数是否是非数字值)

2.string类型：可读不可写

length属性

3.Boolean属性

true和false

4.Undefined类型

var一个变量却没赋值，此时为undefined类型

5.Null类型

声明变量后赋值为null 如果打印出来是给你object

js里面null属于对象类型的，但是它不具有对象的共性，所以，单独归为一类。

6.object类型

js中对象类型是一组集合。

var user = {name :"summer",age :18};//json类型

var arr = [1,2,3];

## 六、js1实例

```
    <style>
        .box{
            width:350px;
            height:350px;
            background: url("1.jpg");
        }
    </style>
    
        <div class="box"></div>
    <p>
        <input type="button" value="上">
        <input type="button" value="下">
        <input type="button" value="左">
        <input type="button" value="右">
    </p>
    <script>
        // 获取元素
        var box = document.querySelector(".box");
        var btn = document.querySelectorAll("input");

        // 绑定事件
        btn[0].onclick=function () {
            box.style.backgroundPositionX="0px";
            box.style.backgroundPositionY="0px";
        };
        btn[1].onclick=function () {
            box.style.backgroundPositionX="0px";
            box.style.backgroundPositionY="350px";
        };
        btn[2].onclick=function () {
            box.style.backgroundPositionX="350px";
            box.style.backgroundPositionY="0px";
        };
        btn[3].onclick=function () {
            box.style.backgroundPositionX="350px";
            box.style.backgroundPositionY="350px";
        };
    </script>
```

## 七、js操作符

### 7.1算术运算符

+、-、=、*、/、%、++、--

```
        // 注意：除了+的拼接以外，数和数，数和字符都符合数和数的运算。
        // 数和数
        var n1 = 5;
        var n2 = 8;
		console.log(n1+n2); // 13
        console.log(n1%n2); // 5
        // 数和字符
        var s = "8";
        console.log(n1+s);  // 58
        console.log(n1-s);  // -3
        console.log(n1*s); // 40
        //true在电脑里默认为1，false，和null默认为0，undefind拼接起来是nan
        console.log(n1 - true); // 4
        console.log(n1 + false);    // 5
        console.log(n1 + null);// 5
        console.log(n1 + undefined); // NaN
        
        // ++、--
        var n3 = 5;
        // ++自增
        console.log(n3); // 5
        // y = n3++;    // 先返回n3的值，再n3=n3+1
        // console.log(y); // 5
        console.log(n3++); // 5
        console.log(n3); // 6

        console.log("我是分割线");
        console.log(n3); // 6
        console.log(++n3); // 7, 先n3=n3+1，再返回n3的值
        console.log(n3); // 7

        // --自减
        console.log("我是分割线");
        console.log(n3); // 7
        console.log(n3--); // 7 ,先返回n3的值，再n3=n3-1
        console.log(n3); // 6

        console.log("我是分割线三");
        console.log(n3); // 6
        console.log(--n3); // 5，先n3=n3-1，再返回n3的值
        console.log(n3); // 5
```

### 7.2赋值运算符

=、+=、-=、*=、/=

```
        var num=5; // 赋值
        console.log(num);
        num+=1; // ===>num = num + 1
        console.log(num);
        // 比较运算符有: >、>=、
```

### 7.3比较运算符

'>'、>=、<、<=、==、===(全等)

注：===为数值相等并且数据类型也相等

==为数值相等，数据类型不相等

```
        var num = 5;
        var str = 5;
        console.log("我是华丽的分割线");
        if(num === str){ // 数值和数据类型均相同
            console.log("===");
        }else if(num == str){ // 数值相同，但是数据类型不同
            console.log("==");
        }else{
            console.log("不相等");
        }
```

逻辑运算符

&&(与）、||（或）、|（非）

```
   		// a&&b：假如a可以转换为false则返回a值，否则返回b；
        console.log(10&&0&&8); // 0
        console.log(10&&8&&undefined); // undefined

        // a||b:假如a可以转换为true则返回a值，否则返回b；
        console.log(10||0||8); // 10
        console.log(undefined||8||10); // 8

        // ！（非）取反
        console.log(!false); // true
        console.log(!0); // true
        console.log(!true); // false
```

## 八、控制流程

### 8.1 if else

```
<script>
    var name = "朦胧";
    if(name === "飞飞"){
        console.log(name + "好漂亮");
    }else if(name==="朦胧"){
        console.log(name+"美丽");
    }else{
        console.log("who?");
    }
    // 三目运算
    if(name){
        console.log(name+'好');
    }
    // 上例优化写法
    if(name)console.log(name+'好');

    if(name === "朦胧"){
        console.log(name + "好漂亮");
    }else{
        console.log(name + "好帅气");
    }
    // 上例优化写法
    name === "朦胧"?console.log(name + "好漂亮"):console.log(name + "好帅气");
</script>
```

### 8.2 switch

```
<script>
    var name = "邱子宸";
    switch (name) {
        case "朦胧":
            console.log(name+"好漂亮");
            break;
        case "邱子宸":
            console.log(name+"好帅气");
            break;
        case "tomas":
            console.log(name+"小鲜肉");
            break;
        default（默认）:
            console.log("who?");
            break;
    }
```

## 九、循环

```
    <style>
        ul{
            list-style: none;
        }
        li{
            height:15px;
            width:15px;
            border:1px solid black;
            border-radius:50%;
            float:left;
            margin-left:5px;
        }
    </style>


    <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    
    
<script>
    // for(var i=1;i<10;i++){
    //     for(var j=1;j<10;j++){
    //         console.log(i+":"+j);
    //     }
    // }
    // 原始方法
    // var btn = document.querySelectorAll("li");
    // btn[0].onclick = function () {
    //     alert("1");(alert可以给你小窗口，然后显示该东西)
    // };
    // btn[1].onclick =function(){
    //     alert("2");
    // };
    // btn[2].onclick =function(){
    //     alert("3");
    // };
    // btn[3].onclick =function(){
    //     alert("4");
    // };
    
    // for循环+点击事件:
    //实现轮播图点击事件
    // let :块级作用域：for后面的花括号的作用域；此时如果用var，他只能执行行的作用域，let为块级，这样才可以执行块级作用域
    var btn = document.querySelectorAll("li");
    for(let i=0;i<btn.length;i++){
        btn[i].onclick=function () {
            console.log(i);
        }
    }
    // while
    var i = 10;
    while(i<10){
        console.log(i);
        i++; // 结束条件
    }
    //do...while
    var i=10;
    do{
        alert(i);
        i++;
    }while(i<10)
    
```

## 十、字符串方法

下标查找

字符串查找下标（可以定义起点）

切割 split，返回数组

切片：substring：包前不包后，会比较数值的大小，小的放前面，负数变为0。单参数：截取当前序列至末尾的字符串

slice：包前不包后，不会进行数值的自动转换（必须是前小后大，否则拿不到值），负数表示从后往前数。单参数：截取当前序列至末尾的字符串

```
<script>
    var str = "wo xue guo python";
    // length:包括空格
    console.log(str.length); // 17
    // 字符串可读
    console.log(str[5]); // e
    // 字符串不可写
    str[5] = "6";
    console.log(str[5]); // e
    console.log(str); // e

    // 索引:第一个参数，你想要查找的字符或者字符串。第二个可选参数，表示开始查找的下标。查找成功返回第一个索引，否则返回-1。
    console.log(str.indexOf("e"));
    console.log(str.indexOf("o"));
    console.log(str.indexOf("o",5)); // 9
    console.log(str.indexOf("e",6)); // -1

    // split 切割
    console.log(str.split(" "));    // 数组["wo", "xue", "guo", "python"]

    // 切片：substring、slice
    // substring
    // 包前不包后，会比较数值的大小，小的放前面，负数变为0
    console.log(str.substring(1,6)); //o xue
    console.log(str.substring(-2,6)); // wo xue
    console.log(str.substring(6,-2)); // wo xue
    // 单参数：截取当前序列至末尾的字符串
    console.log(str.substring(6)); //  guo python

    // slice
    // 包前不包后，不会进行数值的自动转换（必须是前小后大，否则拿不到值），负数表示从后往前数
    console.log(str.slice(1,6)); //o xue
    console.log(str.slice(-2,6)); // 无
    console.log(str.slice(6,-2)); //  guo pyth
    // 单参数：截取当前序列至末尾的字符串
    console.log(str.slice(6)); // guo python
</script>
```

## 十一、js2实例

```
        .middle .content .left .banner img{
            display:none;
        }
        .middle .content .left .banner img.show{
            display:block;
        }
        
        <li><img class="show" src="https://res.shiguangkey.com//file/201806/19/20180619141337485823895.jpg" alt=""></li>
        
        var tab = document.querySelectorAll(".tab li");
        var pic = document.querySelectorAll(".pic img");
        for(let i=0;i<tab.length;i++){
            tab[i].onclick=function () {
                for(let j=0;j<pic.length;j++){
                    if(i===j){
                        pic[j].className="show";
                    }else{
                        pic[j].className="";
                    }
                }
            };
        }
```

## 十二、数组方法

数组常用方法：

### 1.length() 长度

### 2.[] 下标

### 3.push()追加

### 4.unshift()添加

### 5.pop()后删

会返回删除的值

### 6.shift()前删

会返回删除的值

### 7.indexof()索引

### 8.slice()切片

### 9.splice()替换

传一个参数n,表示数组从0开始截取n位

传两个参数a,b,表示数组从a下标开始删除b位

传三个参数a,b,c(替换）,表示数组从a下标开始删除b位,并在删除的位置填入了c，c可以是多个值

### 10.join()拼接

b.join("+")就是在数组中间都加上'+'

### 11.sort()排序：通过ASCII码排序

数学排序

a.sort(function(s,y)){

逆序：return x-y;

正序：return y-x;

}

### 12.reverse()反向

### 13.concat()连接

```
<script>
    // 数组的创建
    var a = [];
    var b = new Array();
    //数组的操作方法
    obj = [1, 5, 8, 9];
    console.log(obj.length);
    // 数组的可读和可写
    console.log(obj[2]);
    obj[2]="c";
    console.log(obj);
    // 添加
    obj.push("a", "b");
    console.log(obj);
    obj.unshift("e", "f");
    console.log(obj);
    // 移出
    x = obj.pop();
    console.log(x);
    console.log(obj);
    y = obj.shift();
    console.log(y);
    console.log(obj);
    // splice()
    console.log(obj); // ["f", 1, 5, "c", 9, "a"]
    // 传一个参数n,表示数组从0开始截取n位
    // obj.splice(2);
    // console.log(obj); // ["f", 1]
    // 传两个参数a,b,表示数组从a下标开始删除b位
    // obj.splice(2,2);
    // console.log(obj); //  ["f", 1, 9, "a"]
    // 传三个参数a,b,c(替换）,表示数组从a下标开始删除b位,并在删除的位置填入了c，c可以是多个值
    obj.splice(2,2,"f","g","h");
    console.log(obj);

    // 排序：sort（）reverse（）通过Ascii码进行排序
    // Ascii码排序
    var a = [0, -1, 4, -8];
    console.log(a.sort()); //[-1, -8, 0, 4]
    console.log(a.reverse());//[4, 0, -8, -1]

    // 数学排序
    a.sort(function (x,y) {
        // return x-y;
        return y-x;
    });
    console.log(a); //  [-8, -1, 0, 4]

    // join
    b = ["a", "b", "d","n"];
    console.log(b.join("+"));//a+b+d+n
</script>
```

## 十三、补充方法

```
<script>
	zc.innerHTML="<span>敌军还有</span>"+i+"<span>秒到达战场</span>";
	//注：只有在innerhtml时才可以添加span标签



    var a = 123.456;
    // toString:转换字符串
    var b = a.toString();
    console.log(b);//123.456
    console.log((typeof a));//number
    console.log((typeof b));//string

    //toFixed：小数字符串
    var c = a.toFixed(2);//不传参表示没有小数位数。传几个表示显示几个小数
    console.log(c);
    console.log((typeof a));//number
    console.log((typeof c));//string

    // parseInt:整数
    // parseFloat:浮点数
    var d = "123456.7c9";
    var e = "123a56.789";
    console.log(parseInt(d)); // 123456
    console.log(parseInt(e)); // 123
    console.log(parseFloat(d)); // 123456.7
    console.log(parseFloat(e)); // 123

    // Number()：类型转换，其他的数据类型强制转换为数字类型
    console.log(Number(b)); // 123.456
    console.log(Number(e));//NaN
    console.log(typeof Number(b))//number

    // isNaN:判断是否为not a number
    console.log(isNaN(e)); // true

</script>
```

## 十四、math方法

### round:四舍五入

### floor：天花板，向下取整

### ceil：地板，向上取整

```
<script>
    // random和取整三个方法
    // 取整：round：四舍五入、floor（地板,向下取整）、ceil（天花板，向上取整）
    console.log(Math.round(123.623)); // 124
    console.log(Math.floor(123.623)); // 123
    console.log(Math.ceil(123.123)); // 124

    // 随机数
    console.log(Math.random()); // 0-1
    console.log(Math.random()*10); // 0-10
    
    // 随机数取整
    console.log(Math.round(Math.random()*10));
    console.log(parseInt(Math.random()*10));
</script>
```

## 十五、日期对象

### 年：time.getFullYea

### 月：time.getMonth

### 日：time.getDate

### 时：time.getHours

### 分：time.getMinutes

### 秒：time.getSeconds

### 在body中显示文字：document.body.innerText

```
<script>
    // 获取时间对象
    var time = new Date();
    // 当前的时间
    console.log(time);
    // 时间戳
    console.log(time.getTime());
    // 年月日时分秒,月份和星期都是从0开始计算。
    var year = time.getFullYear();
    var month = time.getMonth()+1;
    var date = time.getDate();
    var hour = time.getHours();
    var min = time.getMinutes();
    var sec = time.getSeconds();
    // 打印
    console.log(year+"年"+month+"月"+date+"日"+hour+"时"+min+"分"+sec+"秒"); // 2019年7月20日21时44分35秒
    // 页面显示
    document.body.innerText=year+"年"+month+"月"+date+"日"+hour+"时"+min+"分"+sec+"秒";

</script>
```

## 十六、：定时器

### 设置延时器：setTimeout(f,毫秒)

### 清除延时器:clearTimeout

清除定时器：1.定时器命名2.清除

### 设置定时器:setInterval(f,毫秒)

### 清除定时器:clearInterval

```
<input type="button" value="停止">

<script>
    //setTimeout(f,毫秒):延迟1s后再执行函数
    // setTimeout(function () {
    //     console.log("ok");
    // },1000);
    //setInterval(f,毫秒):每隔1s执行一次函数
    // setInterval(function () {
    //     console.log("ok");
    // }, 1000);
    这个每隔一秒去执行一次函数
    // 改造下
    function f(){
        console.log("ok");
    }
    // setTimeout(f,1000);
    // setInterval(f,1000);
    // 清除定时器：1.定时器命名2.清除
    // var st = setTimeout(f,1000);
    // clearTimeout(st);
    // var si = setInterval(f,1000);
    // var btn = document.querySelector("input");
    // btn.onclick=function () {
    //     clearInterval(si);
    // }
</script>
```

## 十七、函数

### 17.1、函数

前段里面，函数调用在函数前面和后面都可以。

```
<script>
    f();
    // 函数定义
    // 有名函数
    function f() {
        console.log("ok");
    }
    // 函数执行
    // f();
   // 匿名函数
   // obj.onclick=function () {
   //     console.log("匿名函数");
   // }
   // 有名函数调用是函数名+（）
    // 匿名函数我也想像有名函数一样执行
    // 1.匿名函数加上（+，-，！，~，())--->函数表达式
    // 2.函数表达式()
    // +function(){
    //     alert("1");
    // }();
    第一种
    // (function(){
    //     alert("2");
    // })();
    第二种
    // (function(){
    //     alert("1");
    // }());

    // 函数参数
    function sum(x,y,z){
        var s = x+y+z;
        console.log(s);
        console.log("x:"+x+";y:"+y+";z:"+z);
    }
    // sum(1,2,3); // 6 x:1;y:2;z:3
    // sum(1,2);//NaN x:1;y:2;z:undefined
    // sum(1,2,3,4); // 6 x:1;y:2;z:3

    // 优化
    function sum(){
        console.log(arguments);
        console.log(arguments.length);
        var s = 0;
        for(var i=0;i<arguments.length;i++){
            s += arguments[i];
        }
        console.log(s);
        return("我return什么，返回值就是什么")
        // var s = x+y+z;
        // console.log(s);
        // console.log("x:"+x+";y:"+y+";z:"+z);
    }
    y = sum(1,2,3); //
    console.log("返回值："+y); // 不用return，undefined；用return，return什么，返回值就是什么
    sum(1,2);//
    sum(1,2,3,4); //
</script>
```

### 17.2、函数作用域

函数：先找function，然后进行声明变量，最后进行函数的执行。

外面var全局变量整个js生效，函数内var函数内生效

变量都有自己的作用范围，函数内var的变量，它的作用范围就是函数本身，外部是访问不到；

```
<script>
        // f();
        // function f() {
        //     console.log(a); // undefined
        //     var a = "ok";
        //     console.log(a); // "ok"
        // }


        /*
        提前声明：函数执行前，所有的变量都进行了声明，但未赋值
        1.function f + var a---->a==undefined;
        2.函数从上往下执行
        */

        // function a() {
        //     console.log("ok");
        // }
        // a();
        // function a() {
        //     console.log("hello");
        // }
        // a();//此时打印两个hello

        /*
        1.function a ---->console.log("ok");
          function a ---->console.log("hello");
          =====> a ----->console.log("hello");
         2. a();====>console.log("hello");
            a();====>console.log("hello");
        */

        function a() {
            console.log("ok");
        }
        a();
        function a() {
            console.log("hello");
        }
        a();
        var a=function () {
            console.log("hi");
        };
        a();

        /* 变量和函数
        1.function a ---->console.log("ok");
          function a ---->console.log("hello");
          =====>function a ----->console.log("hello");
          var a;变量
         2. a();===>function a ----->console.log("hello");
            a();=====>function a ----->console.log("hello");
            a变量赋值=console.log("hi");
            a();====>console.log("hi");
        */

        // 外面var全局变量整个js生效，函数内var函数内生效
        var name="阙林国";
        function f() {
            var name="张学成";
            console.log("1:"+name);
        }
        console.log("2:"+name);
        f();
        console.log("3:"+name);

        /*
        1.var name="阙林国";
          function f + var name
        2.执行
          console.log("2:"+name);===>"2:阙林国"
          f();===>name="张学成";console.log("1:"+name);===>1:张学成
          console.log("3:"+name);====>3:阙林国
        */
        // 变量都有自己的作用范围，函数内var的变量，它的作用范围就是函数本身，外部是访问不到；

    </script>
```

## 十八、iframe

实现局部刷新，但不会用会使用ajxs，这个不太安全

```
    <div>这是我自己的</div>
    <iframe src="0-form.html" frameborder="0" style="width:100%; height:1200px;"></iframe>
    <div>这是我自己的</div>
    <!--<iframe src="https://music.163.com/" frameborder="0" style="width:100%; height:1200px;"></iframe>-->
```

