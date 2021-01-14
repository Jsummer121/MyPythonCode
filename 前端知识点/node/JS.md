# JS

## 一、JavaScript介绍

JavaScript是运行在浏览器端的脚步语言，JavaScript主要解决的是前端与用户交互的问题，包括使用交互与数据交互。 JavaScript是浏览器解释执行的，前端脚本语言还有JScript（微软，IE独有），ActionScript( Adobe公司，需要插件)等。

**前端三大块**
1、HTML：页面结构
2、CSS：页面表现：元素大小、颜色、位置、隐藏或显示、部分动画效果
3、JavaScript：页面行为：部分动画效果、页面与用户的交互、页面功能

## 二、JavaScript嵌入页面的方式

1、行间事件（主要用于事件）

```
<input type="button" name="" onclick="alert('ok！');">
```

2、页面script标签嵌入

```
<script type="text/javascript">        
    alert('ok！');
</script>
```

3、外部引入

```
<script type="text/javascript" src="js/index.js"></script>
```

## 三、变量

JavaScript 是一种弱类型语言，javascript的变量类型由它的值来决定。 定义变量需要用关键字 'var'

```
 var iNum = 123;
 var sTr = 'asd';

 //同时定义多个变量可以用","隔开，公用一个‘var’关键字

 var iNum = 45,sTr='qwe',sCount='68';
```

**变量类型**

5种基本数据类型：
1、number 数字类型
2、string 字符串类型
3、boolean 布尔类型 true 或 false
4、undefined undefined类型，变量声明未初始化，它的值就是undefined
5、null null类型，表示空对象，如果定义的变量将来准备保存对象，可以将变量初始化为null,在页面上获取不到对象，返回的值就是null

1种复合类型：
object

**javascript语句与注释**

1、一条javascript语句应该以“;”结尾

```
<script type="text/javascript">    
var iNum = 123;
var sTr = 'abc123';
function fnAlert(){
    alert(sTr);
};
fnAlert();
</script>
```

2、javascript注释

```
<script type="text/javascript">    

// 单行注释
var iNum = 123;
/*  
    多行注释
    1、...
    2、...
*/
var sTr = 'abc123';
</script>
```

**变量、函数、属性、函数参数命名规范**

1、区分大小写
2、第一个字符必须是字母、下划线（_）或者美元符号（$）
3、其他字符可以是字母、下划线、美元符或数字

**匈牙利命名风格：**

对象o Object 比如：oDiv
数组a Array 比如：aItems
字符串s String 比如：sUserName
整数i Integer 比如：iItemCount
布尔值b Boolean 比如：bIsComplete
浮点数f Float 比如：fPrice
函数fn Function 比如：fnHandler
正则表达式re RegExp 比如：reEmailCheck

## 四、获取元素方法一

可以使用内置对象document上的getElementById方法来获取页面上设置了id属性的元素，获取到的是一个html对象，然后将它赋值给一个变量，比如：

```
<script type="text/javascript">
    var oDiv = document.getElementById('div1');
</script>
....
<div id="div1">这是一个div元素</div>
```

上面的语句，如果把javascript写在元素的上面，就会出错，因为页面上从上往下加载执行的，javascript去页面上获取元素div1的时候，元素div1还没有加载，解决方法有两种：

第一种方法：将javascript放到页面最下边

```
....
<div id="div1">这是一个div元素</div>
....

<script type="text/javascript">
    var oDiv = document.getElementById('div1');
</script>
</body>
```

第二种方法：将javascript语句放到window.onload触发的函数里面,获取元素的语句会在页面加载完后才执行，就不会出错了。

```
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
    }
</script>

....

<div id="div1">这是一个div元素</div>
```

## 五、操作元素属性

获取的页面元素，就可以对页面元素的属性进行操作，属性的操作包括属性的读和写。

**操作属性的方法**
1、“.” 操作
2、“[ ]”操作

**属性写法**

1、html的属性和js里面属性写法一样
2、“class” 属性写成 “className”
3、“style” 属性里面的属性，有横杠的改成驼峰式，比如：“font-size”，改成”style.fontSize”

通过“.”操作属性：

```
<script type="text/javascript">

    window.onload = function(){
        var oInput = document.getElementById('input1');
        var oA = document.getElementById('link1');
        // 读取属性值
        var sValue = oInput.value;
        var sType = oInput.type;
        var sName = oInput.name;
        var sLinks = oA.href;
        // 写(设置)属性
        oA.style.color = 'red';
        oA.style.fontSize = sValue;
    }

</script>

......

<input type="text" name="setsize" id="input1" value="20px">
<a href="http://www.itcast.cn" id="link1">传智播客</a>
```

通过“[ ]”操作属性：

```
<script type="text/javascript">

    window.onload = function(){
        var oInput1 = document.getElementById('input1');
        var oInput2 = document.getElementById('input2');
        var oA = document.getElementById('link1');
        // 读取属性
        var sVal1 = oInput1.value;
        var sVal2 = oInput2.value;
        // 写(设置)属性
        // oA.style.val1 = val2; 没反应
        oA.style[sVal1] = sVal2;        
    }

</script>

......

<input type="text" name="setattr" id="input1" value="fontSize">
<input type="text" name="setnum" id="input2" value="30px">
<a href="http://www.itcast.cn" id="link1">传智播客</a>
```

**innerHTML**
innerHTML可以读取或者写入标签包裹的内容

```
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>

......

<div id="div1">这是一个div元素</div>
```

## 六、函数

函数就是重复执行的代码片。

**函数定义与执行**

```
<script type="text/javascript">
    // 函数定义
    function fnAlert(){
        alert('hello!');
    }
    // 函数执行
    fnAlert();
</script>
```

**变量与函数预解析**
JavaScript解析过程分为两个阶段，先是编译阶段，然后执行阶段，在编译阶段会将function定义的函数提前，并且将var定义的变量声明提前，将它赋值为undefined。

```
<script type="text/javascript">    
    fnAlert();       // 弹出 hello！
    alert(iNum);  // 弹出 undefined
    function fnAlert(){
        alert('hello!');
    }
    var iNum = 123;
</script>
```

**提取行间事件**
在html行间调用的事件可以提取到javascript中调用，从而做到结构与行为分离。

```
<!--行间事件调用函数   -->
<script type="text/javascript">        
    function fnAlert(){
        alert('ok!');
    }
</script>
......
<input type="button" name="" value="弹出" onclick="fnAlert()">

<!-- 提取行间事件 -->
<script type="text/javascript">

window.onload = function(){
    var oBtn = document.getElementById('btn1');
    oBtn.onclick = fnAlert;
    function fnAlert(){
        alert('ok!');
    }
}    
</script>
......
<input type="button" name="" value="弹出" id="btn1">
```

**匿名函数**

定义的函数可以不给名称，这个叫做匿名函数，可以将匿名函数直接赋值给元素绑定的事件来完成匿名函数的调用。

```
<script type="text/javascript">

window.onload = function(){
    var oBtn = document.getElementById('btn1');
    /*
    oBtn.onclick = myalert;
    function myalert(){
        alert('ok!');
    }
    */
    // 直接将匿名函数赋值给绑定的事件

    oBtn.onclick = function (){
        alert('ok!');
    }
}

</script>
```

**综合练习**
网页换肤

**函数传参**

```
<script type="text/javascript">
    function fnAlert(a){
        alert(a);
    }
    fnAlert(12345);
</script>
```

**函数'return'关键字**
函数中'return'关键字的作用：
1、返回函数执行的结果
2、结束函数的运行
3、阻止默认行为

```
<script type="text/javascript">
function fnAdd(iNum01,iNum02){
    var iRs = iNum01 + iNum02;
    return iRs;
    alert('here!');
}

var iCount = fnAdd(3,4);
alert(iCount);  //弹出7
</script>
```

## 七、条件语句

通过条件来控制程序的走向，就需要用到条件语句。

**运算符**
1、算术运算符： +(加)、 -(减)、 *(乘)、 /(除)、 %(求余)
2、赋值运算符：=、 +=、 -=、 *=、 /=、 %=
3、条件运算符：`==`、`===`、>、>=、<、<=、!=、&&(而且)、||(或者)、!(否)

**if else**

```
var iNum01 = 3;
var iNum02 = 5;
var sTr;
if(iNum01>iNum02){
    sTr = '大于';
}
else
{
    sTr = '小于';
}
alert(sTr);
```

**理解练习**
制作单个按钮点击切换元素的显示和隐藏效果

**多重if else语句**

```
var iNow = 1;
if(iNow==1)
{
    ... ;
}
else if(iNow==2)
{
    ... ;
}
else
{
    ... ;
}
```

**switch语句**
多重if else语句可以换成性能更高的switch语句

```
var iNow = 1;

switch (iNow){
    case 1:
        ...;
        break;
    case 2:
        ...;
        break;    
    default:
        ...;
}
```

## 八、数组及操作方法

数组就是一组数据的集合，javascript中，数组里面的数据可以是不同类型的。

**定义数组的方法**

```
//对象的实例创建
var aList = new Array(1,2,3);

//直接量创建
var aList2 = [1,2,3,'asd'];
```

**操作数组中数据的方法**
1、获取数组的长度：aList.length;

```
var aList = [1,2,3,4];
alert(aList.length); // 弹出4
```

2、用下标操作数组的某个数据：aList[0];

```
var aList = [1,2,3,4];
alert(aList[0]); // 弹出1
```

3、join() 将数组成员通过一个分隔符合并成字符串

```
var aList = [1,2,3,4];
alert(aList.join('-')); // 弹出 1-2-3-4
```

4、push() 和 pop() 从数组最后增加成员或删除成员

```
var aList = [1,2,3,4];
aList.push(5);
alert(aList); //弹出1,2,3,4,5
aList.pop();
alert(aList); // 弹出1,2,3,4
```

5、unshift()和 shift() 从数组前面增加成员或删除成员

```
var aList = [1,2,3,4];
aList.unshift(5);
alert(aList); //弹出5,1,2,3,4
aList.shift();
alert(aList); // 弹出1,2,3,4
```

6、reverse() 将数组反转

```
var aList = [1,2,3,4];
aList.reverse();
alert(aList);  // 弹出4,3,2,1
```

7、indexOf() 返回数组中元素第一次出现的索引值

```
var aList = [1,2,3,4,1,3,4];
alert(aList.indexOf(1));
```

8、splice() 在数组中增加或删除成员

```
var aList = [1,2,3,4];
aList.splice(2,1,7,8,9); //从第2个元素开始，删除1个元素，然后在此位置增加'7,8,9'三个元素
alert(aList); //弹出 1,2,7,8,9,4
```

**多维数组**
多维数组指的是数组的成员也是数组的数组。

```
var aList = [[1,2,3],['a','b','c']];

alert(aList[0][1]); //弹出2;
```

批量操作数组中的数据，需要用到循环语句

## 九、循环语句

程序中进行有规律的重复性操作，需要用到循环语句。

**for循环**

```
for(var i=0;i<len;i++)
{
    ......
}
```

**while循环**

```
var i=0;

while(i<8){
    ......
    i++;
}
```

**数组去重**

```
var aList = [1,2,3,4,4,3,2,1,2,3,4,5,6,5,5,3,3,4,2,1];

var aList2 = [];

for(var i=0;i<aList.length;i++)
{
    if(aList.indexOf(aList[i])==i)
    {
        aList2.push(aList[i]);
    }
}

alert(aList2);
```

## 十、获取元素方法二

可以使用内置对象document上的getElementsByTagName方法来获取页面上的某一种标签，获取的是一个选择集，不是数组，但是可以用下标的方式操作选择集里面的标签元素。

```
<script type="text/javascript">
    window.onload = function(){
        var aLi = document.getElementsByTagName('li');
        // aLi.style.backgroundColor = 'gold'; // 出错！不能同时设置多个li
        alert(aLi.length);
        aLi[0].style.backgroundColor = 'gold';
    }
</script>
....
<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
    <li>6</li>
</ul>
```

## 十一、Javascript组成

1、ECMAscript javascript的语法（变量、函数、循环语句等语法）
2、DOM 文档对象模型 操作html和css的方法
3、BOM 浏览器对象模型 操作浏览器的一些方法

## 十二、字符串处理方法

1、字符串合并操作：“ + ”

```
var iNum01 = 12;
var iNum02 = 24;
var sNum03 = '12';
var sTr = 'abc';
alert(iNum01+iNum02);  //弹出36
alert(iNum01+sNum03);  //弹出1212 数字和字符串相加等同于字符串相加
alert(sNum03+sTr);     // 弹出12abc
```

2、parseInt() 将数字字符串转化为整数

```
var sNum01 = '12';
var sNum02 = '24';
var sNum03 = '12.32';
alert(sNum01+sNum02);  //弹出1224
alert(parseInt(sNum01)+parseInt(sNum02))  //弹出36
alert(sNum03)   //弹出数字12 将字符串小数转化为数字整数
```

3、parseFloat() 将数字字符串转化为小数

```
var sNum03 = '12.32'
alert(parseFloat(sNum03));  //弹出 12.32 将字符串小数转化为数字小数
```

4、split() 把一个字符串分隔成字符串组成的数组

```
var sTr = '2017-4-22';
var aRr = sTr.split("-");
var aRr2= sTr.split("");

alert(aRr);  //弹出['2017','4','2']
alert(aRr2);  //弹出['2','0','1','7','-','4','-','2','2']
```

5、charAt() 获取字符串中的某一个字符

```
var sId = "#div1";
var sTr = sId.charAt(0);
alert(sTr); //弹出 #
```

6、indexOf() 查找字符串是否含有某字符

```
var sTr = "abcdefgh";
var iNum = sTr.indexOf("c");
alert(iNum); //弹出2
```

7、substring() 截取字符串 用法： substring(start,end)（不包括end）

```
var sTr = "abcdefghijkl";
var sTr2 = sTr.substring(3,5);
var sTr3 = sTr.substring(1);

alert(sTr2); //弹出 de
alert(sTr3); //弹出 bcdefghijkl
```

8、toUpperCase() 字符串转大写

```
var sTr = "abcdef";
var sTr2 = sTr.toUpperCase();
alert(sTr2); //弹出ABCDEF
```

9、toLowerCase() 字符串转小写

```
var sTr = "ABCDEF";
var sTr2 = sTr.toLowerCase();
alert(sTr2); //弹出abcdef
```

**字符串反转**

```
var str = 'asdfj12jlsdkf098';
var str2 = str.split('').reverse().join('');

alert(str2);
```

## 十三、类型转换

1、直接转换 parseInt() 与 parseFloat()

```
alert('12'+7); //弹出127
alert( parseInt('12') + 7 );  //弹出19 
alert( parseInt(5.6));  // 弹出5
alert('5.6'+2.3);  // 弹出5.62.3
alert(parseFloat('5.6')+2.3);  // 弹出7.8999999999999995
alert(0.1+0.2); //弹出 0.3000000000000004
alert((0.1*100+0.2*100)/100); //弹出0.3
alert((parseFloat('5.6')*100+2.3*100)/100); //弹出7.9
```

2、隐式转换 “==” 和 “-”

```
if('3'==3)
{
    alert('相等');
}

// 弹出'相等'
alert('10'-3);  // 弹出7
```

3、NaN 和 isNaN

```
alert( parseInt('123abc') );  // 弹出123
alert( parseInt('abc123') );  // 弹出NaN
```

## 十四、调试程序的方法

1、alert

2、console.log

3、document.title

## 十五、定时器

**定时器在javascript中的作用**
1、制作动画
2、异步操作
3、函数缓冲与节流

定时器类型及语法

```
/*
    定时器：
    setTimeout  只执行一次的定时器 
    clearTimeout 关闭只执行一次的定时器
    setInterval  反复执行的定时器
    clearInterval 关闭反复执行的定时器

*/

var time1 = setTimeout(myalert,2000);
var time2 = setInterval(myalert,2000);
/*
clearTimeout(time1);
clearInterval(time2);
*/
function myalert(){
    alert('ok!');
}
```

```
<script type="text/javascript">
    window.onload = function(){    
        var oDiv = document.getElementById('div1');
        function timego(){
            var now = new Date();
            var year = now.getFullYear();
            var month = now.getMonth()+1;
            var date = now.getDate();
            var week = now.getDay();
            var hour = now.getHours();
            var minute = now.getMinutes();
            var second = now.getSeconds();
            var str = '当前时间是：'+ year + '年'+month+'月'+date+'日 '+toweek(week)+' '+todou(hour)+':'+todou(minute)+':'+todou(second);
            oDiv.innerHTML = str;
        }
        timego();
        setInterval(timego,1000);
    }

    function toweek(n){
        if(n==0)
        {
            return '星期日';
        }
        else if(n==1)
        {
            return '星期一';
        }
        else if(n==2)
        {
            return '星期二';
        }
        else if(n==3)
        {
            return '星期三';
        }
        else if(n==4)
        {
            return '星期四';
        }
        else if(n==5)
        {
            return '星期五';
        }
        else
        {
            return '星期六';
        }
    }


    function todou(n){
        if(n<10)
        {
            return '0'+n;
        }
        else
        {
            return n;
        }
    }
</script>
......
<div id="div1"></div>
```

4、定时器制作倒计时

```
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        function timeleft(){
            var now = new Date();
            var future = new Date(2016,8,12,24,0,0);
            var lefts = parseInt((future-now)/1000);
            var day = parseInt(lefts/86400);
            var hour = parseInt(lefts%86400/3600);
            var min = parseInt(lefts%86400%3600/60);
            var sec = lefts%60;
            str = '距离2016年9月12日晚24点还剩下'+day+'天'+hour+'时'+min+'分'+sec+'秒';
            oDiv.innerHTML = str; 
        }
        timeleft();
        setInterval(timeleft,1000);        
    }

</script>
......
<div id="div1"></div>
```

## 十六、变量作用域

变量作用域指的是变量的作用范围，javascript中的变量分为全局变量和局部变量。

1、全局变量：在函数之外定义的变量，为整个页面公用，函数内部外部都可以访问。
2、局部变量：在函数内部定义的变量，只能在定义该变量的函数内部访问，外部无法访问。

```
<script type="text/javascript">
    //全局变量
    var a = 12;
    function myalert()
    {
        //局部变量
        var b = 23;
        alert(a);
        alert(b);
    }
    myalert(); //弹出12和23
    alert(a);  //弹出12    
    alert(b);  //出错
</script>
```

## 十七、封闭函数

封闭函数是javascript中匿名函数的另外一种写法，创建一个一开始就执行而不用命名的函数。

一般定义的函数和执行函数：

```
function myalert(){
    alert('hello!');
};

myalert();
```

封闭函数：

```
(function myalert(){
    alert('hello!');
})();
```

还可以在函数定义前加上“~”和“!”等符号来定义匿名函数

```
!function myalert(){
    alert('hello!');
}()
```

**封闭函数的好处**
封闭函数可以创造一个独立的空间，在封闭函数内定义的变量和函数不会影响外部同名的函数和变量，可以避免命名冲突，在页面上引入多个js文件时，用这种方式添加js文件比较安全，比如：

```
var iNum01 = 12;
function myalert(){
    alert('hello!');
}
(function(){
    var iNum01 = 24;
    function myalert(){
        alert('hello!world');
    }
    alert(iNum01);
    myalert()
})()
alert(iNum01);
myalert();
```

## 十八、常用内置对象

1、document

```
document.getElementById //通过id获取元素
document.getElementsByTagName //通过标签名获取元素
document.referrer  //获取上一个跳转页面的地址(需要服务器环境)
```

2、location

```
window.location.href  //获取或者重定url地址
window.location.search //获取地址参数部分
window.location.hash //获取页面锚点或者叫哈希值
```

3、Math

```
Math.random 获取0-1的随机数
Math.floor 向下取整
Math.ceil 向上取整
```