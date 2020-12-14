# jquery

**是js文件，在：https://www.bootcdn.cn.jquery/进行仔细检索，主要有完整版和压缩版，使用jQuery可以写少做多**

## 一、导入

```
$==jequery
$(css选择器)


<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
//自己写的script标签需要在他的下面重写。

如果放在head标签里，必须套个盒子
 $(function (){
        console.log($(".box").text());
        console.log(jQuery(".box").text());
    });
```

正常的操作

```
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
<script>
    // var obj = document.querySelector(".box");
    // console.log(obj.innerText);
    $(document).ready(function () {
        console.log($(".box").text());
        console.log(jQuery(".box").text());
    });/下面是从这个代码转化过来的。

    $(function (){
        console.log($(".box").text());
        console.log(jQuery(".box").text());
    });//如果代码写在前面，那必须使用这样的方式，才能进行完整代码的实验。
</script>
<div class="box">好好学习，天天向上</div>
```



## 二、选择元素

```
基本选择器：标签选择器$('p')，id选择器$('#.id名')，class选择器$('.class名')
层级选择器：子代$('parent>child')，后代$('parent child')，相邻$('prev+next')，兄弟$('prev~siblings')
```

### 筛选器：

```
first、last、eq
$("div").first().css('')：第一个，设置样式
$("div").last().text('')：最后一个，修改元素文本内容
$("div").eq(1).css('')： 指定元素，设置样式


children、find:后代选择器,注意，find必须含参
$(".box").children().css('')：查找他的子代选择器，括号里面可以精确到哪一个选择器。
例如：$(".box").children(".test").css('')
$(".box").find(".test").css('')：注使用find时，必须带参数。


parent、parents、parentsUntil
parent:唯一父级和他以及他的全部子级
$(".div5").parent().css('')：4567
parents：祖先元素及全部后代
$(".div5").parents().css('')：1-7全变
parentsUntil: 祖先元素及全部后代(除掉until指定的元素以及它之前的全部祖先元素）
$(".div5").parentsUntil(".div2").css('')：3-7


siblings:找到全部同级元素//可以用来使用轮播图，获取其他的对象
$(".box2").siblings().css('');
```

```
    <div>元素一</div>
    <div>元素二</div>
    <div>元素三</div>
    <h4>以下为children</h4>
    <div class="box">
        <span>无class</span><br>
        <span class="test">有class</span><br>
        <p>无class</p>
        <p class="test">有class</p>
        <div>无class</div>
        <div class="test">有class</div>
    </div>

    <h4>以下是parent</h4>
    <div class="div1">div1
        <div class="div2">div2
            <div class="div3">div3
                <div class="div4">div4
                    <div class="div5">div5
                        <div class="div6">div6
                            <div class="div7">div7</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <h4>以下是sibling</h4>
    <div>1</div>
    <div class="box2">2</div>
    <div>3</div>
    <div>4</div>
    <div>5</div>

    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        // first、last、eq
        // $("div").first().css('font-size', '30px');//第一个，设置样式
        // $("div").last().text("ok");//最后一个，修改元素文本内容
        // $("div").eq(1).css("color", "skyblue");// 指定元素，设置颜色

        // children、find:后代选择器,注意，find必须含参
        // $(".box").children().css("color", "skyblue");
        // $(".box").children(".test").css("font-size", "20px");
        //
        // $(".box").find(".test").css("color", "red");

        // parent、parents、parentsUntil
        // parent:唯一父级和全部子级
        // $(".div5").parent().css("color","red"); // 4567
        // parents：祖先元素及全部后代
        // $(".div5").parents().css("fontSize", "30px"); //1-7全变
        // parentsUntil: 祖先元素及全部后代(除掉until指定的元素以及它之前的全部祖先元素）
        // $(".div5").parentsUntil(".div2").css("color", "skyblue"); //3-7

        // siblings:找到全部同级元素
        $(".box2").siblings().css("color","red");
    </script>
```

**选择器和筛选器的区别**

**选择器他更利于传参**

```
    <ul>
        <li>足球</li>
        <li>篮球</li>
        <li>乒乓球</li>
    </ul>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $("li:eq(1)").css("color", "skyblue"); // 选择器
        $("li").eq(2).css("color","red"); // 筛选器

        function f(obj, index){
            obj.eq(index).css("color","red");
        }
        f($("li"), 1);
    //    总结
        // 简单操作时，选择器和筛选器效果是一样的
        // 但是在函数操作中，筛选器在字符拼接上有优势
    </script>
```

## 三、属性操作

### 3.1test():取全部的文本内容

只是取文本内容

$("div").text()

### 3.2html():多个元素，取第一个

如果存在标签，那将会将标签也要取出来

$("div").html()

### 3.3val():多个元素，取第一个

$("input").val()

如果要去下面的东西可以在这个后面加上eq

$("input").eq(2).val():取第三个元素

### 3.4 属性的增改查

#### 增： $("li").attr("class", "test");

#### 改$("li").attr("class", "test1"); 
####  查console.log($("li").attr("class")); 

### 3.5 属性的删除

#### $("li").removeAttr("class");



**对class属性进行操作**

### 3.6addClass()：添加class

$("button").eq(0).click(function () {
          $("p").addClass("test");
      });

### 3.7removeClass()：移除class

$("button").eq(1).click(function () {
          $("p").removeClass("test");
      });

### 3.8toggleClass()：一个搞定add和remove

$("button").eq(2).click(function () {
          $("p").toggleClass("test");
      });

```
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .test{
            color:peru;
            font-size:30px;
        }
        .test1{
            color:red;
        }
    </style>
</head>
<body>
    <div>1<span>你好</span></div>
    <div>2</div>
    <input type="text" name="usr"><br>
    <input type="text" name="psw"><br>
    <input class="btn" type="button" value="获取value值">

    <h4>属性操作</h4>
    <ul>
        <li>足球</li>
        <li>篮球</li>
        <li>乒乓球</li>
    </ul>

    <h4>class属性操作</h4>
    <p>我是一段文字</p>
    <button>addClass</button>
    <button>removeClass</button>
    <button>toggleClass</button>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
<script>
    // html():多个元素，取第一个
    console.log($("div").html());
    // text():取全部的文本内容
    console.log($("div").text());
    // val():多个元素，取第一个
    $(".btn").click(function () {
        console.log($("input").val());
    });

    // 属性的增删改查
    $("li").attr("class", "test"); // 增
    $("li").attr("class", "test1"); // 改
    console.log($("li").attr("class")); // 查

    // 删除
     $("li").removeAttr("class");

     // class属性操作addClass()/removeClass().toggleClass()
      $("button").eq(0).click(function () {
          $("p").addClass("test");
      });
      $("button").eq(1).click(function () {
          $("p").removeClass("test");
      });
      $("button").eq(2).click(function () {
          $("p").toggleClass("test");
      });
</script>
```

## 四、css样式操作

### 4.1 获取样式

console.log($("div").css("background-color")); //rgb(135, 206, 235)
console.log($("div").css(["background-color","height", "width"])); 

// {background-color: "rgb(135, 206, 235)", height: "200px", width: "200px"}

### 4.2样式设置

#### 设置单个样式

$("div").css("backgroundColor","red");

#### 设置多个样式

$("div").css({ 
     "backgroundColor":"red",
    "font-size":"30px",
     "text-align":"center",
     "line-height":"200px"
 });

### 4.3位置设置

offset()/position()/scrollTop/scrollLeft

#### offset():距离窗口的top/left值

var $obj=$(".two").offset();
console.log($obj); // {top: 92.53125, left: 8}
console.log($obj.left);
console.log($obj.top);

#### position():定位

**设置多少拿到多少**

var $obj1=$(".two").position();
console.log($obj1); // {top: 20, left: 20}
console.log($obj1.left);
console.log($obj1.top);

###  scrollTop()：滚动条

里面有值就是设置，里面没值就是取值    $("button").eq(0).click(function () {
        alert($(".three").scrollTop()+"px");

});
$("button").eq(1).click(function () {
        $(".three").scrollTop(200);
 });

### height()/width()操作元素的宽和高

里面有值就是设置，里面没值就是取值

$("button").eq(0).click(function () {
        alert($(".three").height()+"px");

});
$("button").eq(1).click(function () {
        $(".three").height(200);
 });

```
    <style>
        /*div{*/
            /*height:200px;*/
            /*width:200px;*/
            /*background: skyblue;*/
        /*}*/
        .one{
            height:200px;
            width:200px;
            background: antiquewhite;
            position:relative;
        }
        .two{
            height:100px;
            width:100px;
            background: peru;
            position:absolute;
            top:20px;
            left:20px;
        }
        .three{
            margin-top:100px;
            border:1px solid red;
            width:100px;
            height:100px;
            overflow: auto;
        }
    </style>
    
        <div>我就是我</div>
    <h4>offset和position</h4>
    <div class="one">
        <div class="two">测试对象</div>
    </div>

    <div class="three">基本选择器：标签选择器$("p")、id选择器$("#id名")、class选择器(".class名")层级选择器：子代$("parent>child")，后代$("parent child")，相邻$("prev+next")，兄弟$("prev~siblings")</div>
    <button>获取scrollTop</button>
    <button>设置scrollTop</button>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        // 获取样式
        // console.log($("div").css("background-color")); //rgb(135, 206, 235)
        // console.log($("div").css(["background-color","height", "width"])); // {background-color: "rgb(135, 206, 235)", height: "200px", width: "200px"}

        // 设置
        // $("div").css("backgroundColor","red");
        // $("div").css({ // 设置多个样式
        //     "backgroundColor":"red",
        //     "font-size":"30px",
        //     "text-align":"center",
        //     "line-height":"200px"
        // });

        // 位置offset()/position()/scrollTop/scrollLeft
        // offset():距离窗口的top/left值
        var $obj=$(".two").offset();
        console.log($obj); // {top: 92.53125, left: 8}
        console.log($obj.left);
        console.log($obj.top);

        // position():定位
        var $obj1=$(".two").position();
        console.log($obj1); // {top: 20, left: 20}
        console.log($obj1.left);
        console.log($obj1.top);

        // scrollTop()/height()/width()
        $("button").eq(0).click(function () {
            alert($(".three").scrollTop()+"px");
            alert($(".three").height()+"px");

        });
        $("button").eq(1).click(function () {
            $(".three").scrollTop(200);
            $(".three").height(200);
        });

    </script>
```

## 五、js和jQuery对象的转换

### 5.1 jq--->js
#### 1.利用数组下标
​    var $div = $("div"); //jq对象
​    var div = $div[0]; // 转换为js对象
​    div.style.color = "red"; // js操作方法

#### 2.通过jq的get方法
 var $div = $("div"); //jq对象
 var div = $div.get(1); // 转换为js对象
 div.style.color = "skyblue";// js操作方法

### 5.2 js--->jq

**js情况下**

var div = document.getElementsByTagName("div");//js对象
var $div = $(div);//jq对象
$div.last().css("color","blue");

**jQuery情况下**

var $obj = $(".box");
    $obj.click(function(){
        var $this = $(this);
        $this.css("fontSize","50px");
    });

### 5.4 this

var obj = document.querySelector(".box");
obj.onclick=function () {
	console.log(this); // this指向obj,打印出他的那一行代码。

};



```
<body>
    <div>元素一</div>
    <div>元素二</div>
    <div class="box">元素三</div>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
<script>
    //jq--->js
    //1.利用数组下标
    var $div = $("div"); //jq对象
    var div = $div[0]; // 转换为js对象
    div.style.color = "red"; // js操作方法

    // 2.通过jq的get方法
     var $div = $("div"); //jq对象
     var div = $div.get(1); // 转换为js对象
     div.style.color = "skyblue";// js操作方法

    //js--->jq
    var div = document.getElementsByTagName("div");//js对象
    var $div = $(div);//jq对象
    $div.last().css("color","blue");

    // this
    var obj = document.querySelector(".box");
    obj.onclick=function () {
        console.log(this); // this指向obj
    };

    var $obj = $(".box");
    $obj.click(function(){
        var $this = $(this);
        $this.css("fontSize","50px");
    });
</script>
```

## 六、标签处理

### 6.1 内部插入：在内容的前后插入

#### 1.append()：在目标元素的内容后添加一个"<p>append</p>"

$(".div3").append("<p>append</p>");

#### 2.appendTo()：将"<p>appendTo</p>"添加到目标元素的内容后

$("<p>appendTo</p>").appendTo(".div3");

#### 3.prepend()：在目标元素的内容前添加一个"<p>prepend</p>"

$(".div3").prepend("<p>prepend</p>")

显示为：<p>append</p>

#### 4.prependTo()：将"<p>prependTo</p>"添加到目标元素的内容前

$("<p>appendTo</p>").appendTo(".div3");



### 6.2 外部插入：在元素的前后插入

#### 1.after:在目标元素后添加一个"<p>after</p>"

$(".div4").after("<p>after</p>");

###  2.before:在目标元素前添加一个"<p>before</p>"

$(".div4").before("<p>before</p>");

#### 3.insertBefore()：把"<p>insertBefore</p>"插入到目标元素

 $("<p>insertBefore</p>").insertBefore(".div4");

#### 4. insertAfter()：把"<p>insertAfter</p>"插入到目标元素

$("<p>insertAfter</p>").insertAfter(".div4");



 ### 6.3

#### 1.replaceWith():替换标签及内容

$(".div3").replaceWith("<p>我是来替换div3的</p>")

#### 2.remove():移除标签及内容

$(".div2").remove();

#### 3.empty():清空标签内容（标签保留）

$(".div4").empty();
#### 4.clone()：
$(".div5").clone().appendTo("p");

```
<body>
    <div class="div1">
        <div class="div2">div2</div>
        <div class="div3">div3</div>
        <div class="div4">div4</div>
        <div class="div5">div5</div>
    </div>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        // 内部插入：append()/appendTo()/prepend()/prependTo()
        // 在目标元素的内容后添加一个"<p>append</p>"
        // $(".div3").append("<p>append</p>");
        // prepend()在目标元素的内容前添加一个"<p>prepend</p>"
        //  $(".div3").prepend("<p>prepend</p>");
         // appendTo():将"<p>appendTo</p>"添加到目标元素的内容后
        // $("<p>appendTo</p>").appendTo(".div3");
        // prependTo():将"<p>prependTo</p>"添加到目标元素的内容前
        // $("<p>prependTo</p>").prependTo(".div3");

        // 外部插入：before()/insertBefore()/after()/insertAfter()/replaceWith()/remove()/empty()/clone()
        // before()/insertBefore()/after()/insertAfter()
        //  after:在目标元素后添加一个"<p>after</p>"
        //  before:在目标元素前添加一个"<p>before</p>"
        // $(".div4").after("<p>after</p>");
        // $(".div4").before("<p>before</p>");
        // insertBefore()
        // insertAfter()
        // $("<p>insertBefore</p>").insertBefore(".div4");
        // $("<p>insertAfter</p>").insertAfter(".div4");

        // replaceWith()/remove()/empty()/clone()
        // replaceWith():替换标签及内容
         $(".div3").replaceWith("<p>我是来替换div3的</p>")
        // remove():移除标签及内容
        $(".div2").remove();
        // empty():清空标签内容（标签保留）
        $(".div4").empty();
        // clone()
        $(".div5").clone().appendTo("p");
    </script>
```

## 七、事件操作

### 7.1.each：遍历

 $("li").each(function (index) {
		console.log(index);
});

### 7.2for循环+绑定事件，jQuery可以直接在function里面拿到index

**之前**

var btn = document.querySelectorAll("li");
 for(let i=0; i<btn.length;i++){
     btn[i].onclick=function () {
        console.log(i);
     }
 }

**现在**

$("li").each(function (index) {
     $("li").eq(index).click(function () {
      	 console.log(index);
     });
});

### 7.3index

$("li").click(function () {
     console.log($(this).index());
 });

### 7.4鼠标的移入移出事件hover

// 语法格式：$("div").hover(f1,f2);

$("div").hover(function () {
    console.log("我是鼠标移入函数");
},function () {
    console.log("我是鼠标移出函数");
});

```
    <style>
        ul{
            list-style:none;
        }
        li{
            height:20px;
            width:20px;
            background:#a7ca1b;
            float:left;
            margin-left:10px;
        }
        div{
            height:100px;
            width:100px;
            background: #a7ca1b;
        }
    </style>
    
    <body>
    <!--<ul>-->
        <!--<li></li>-->
        <!--<li></li>-->
        <!--<li></li>-->
        <!--<li></li>-->
    <!--</ul>-->

    <div>我就是我</div>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        // each遍历
        // $("li").each(function (index) {
        //     console.log(index);
        // });
        // for循环+绑定事件
        // var btn = document.querySelectorAll("li");
        // for(let i=0; i<btn.length;i++){
        //     btn[i].onclick=function () {
        //         console.log(i);
        //     }
        // }
        // $("li").each(function (index) {
        //     $("li").eq(index).click(function () {
        //         console.log(index);
        //     });
        // });

        // index
        // $("li").click(function () {
        //     console.log($(this).index());
        // });

        // 鼠标的移入移出事件hover
        // $("div").hover(f1,f2);
        $("div").hover(function () {
            console.log("我是鼠标移入函数");
        },function () {
            console.log("我是鼠标移出函数");
        });
    </script>
```

## 八、动画

### 8.1隐藏和显示

var $box = $(".box1");

#### 1.隐藏hide（）里面可以设置动画时间
$("button").first().click(function () {
	$box.hide(3000);
});

#### 2.显示show（）里面可以设置动画时间

$("button").eq(1).click(function () {
    $box.show(3000);
});

#### 3.切换

$("button").eq(2).click(function () {
    $box.toggle(3000);
});



### 8.2淡入淡出：括号里面的数字为时间

var $button = $(".box3>button");

### 1.淡出fadeOut

$button.first().click(function () {

​	$box.fadeOut(3000).css("backgroundColor", "red");
});

### 2.淡入fadeIn

$button.eq(1).click(function () {
        $box.fadeIn(3000).css("backgroundColor", "skyblue");
});

### 3.切换fadeToggle

#### 3.1普通

$button.eq(2).click(function () {
        $box.fadeToggle(3000).css("backgroundColor", "skyblue");
});

#### 3.2进阶fadeTo

$button.eq(3).click(function () {
        $(".div1").fadeTo("slow",0.15);
        $(".div2").fadeTo("slow",0.5);
        $(".div3").fadeTo("slow",0.7);
});

### 8.3.滑动

var $button = $(".box5>button");

var $box = $(".box4");

#### 1.下滑

$button.first().click(function () {
   $box.slideDown("slow");
});

#### 2.上拉

$button.eq(1).click(function () {
    $box.slideUp("slow");
});

#### 3.切换

$button.eq(2).click(function () {
    $box.slideToggle("slow");
});

## 8.4 自定义动画animate

var $button = $(".box6>button");

$button.first().click(function () {
    $box.animate({height:"300px"}).delay(5000); // 延迟5s后再发生下一个动画
});

$button.eq(1).click(function () {
    $box.animate({height:"200px"});
});

```
    <style>
        .box1{
            height:400px;
            width:400px;
            background: skyblue;
        }
        .div1,.div2,.div3{
            height:100px;
            width:100px;
        }
    </style>
    <div class="box1">
        <div class="div1" style="background: #a7ca1b"></div>
        <div class="div2" style="background: red"></div>
        <div class="div3" style="background: blue"></div>
    </div>
    <div class="box2">
        <button>隐藏</button>
        <button>显示</button>
        <button>切换</button>
    </div>
    <div class="box3">
        <button>淡出</button>
        <button>淡入</button>
        <button>切换</button>
        <button>fadeTo</button>
    </div>

    <div class="box4" style="height:200px;width:200px;background: peru; display: none;">
        <h4>标题</h4>
        <p>段落一</p>
        <p>段落二</p>
    </div>
    <div class="box5">
        <button>slideDown</button>
        <button>slideUp</button>
        <button>slideToggle</button>
    </div>
    <div class="box6">
        <button>自定义动画1</button>
        <button>自定义动画2</button>
    </div>

<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
<script>
    // 隐藏和显示
    var $box = $(".box1");
    $("button").first().click(function () {
        $box.hide(3000);
    });
    $("button").eq(1).click(function () {
        $box.show(3000);
    });
    $("button").eq(2).click(function () {
        $box.toggle(3000);
    });
    // 淡入淡出:fadeOut/fadeIn/fadeToggle/fadeTo
    var $button = $(".box3>button");
    $button.first().click(function () {
        $box.fadeOut(3000).css("backgroundColor", "red");
    });
    $button.eq(1).click(function () {
        $box.fadeIn(3000).css("backgroundColor", "skyblue");
    });
    $button.eq(2).click(function () {
        $box.fadeToggle(3000).css("backgroundColor", "skyblue");
    });
    $button.eq(3).click(function () {
        $(".div1").fadeTo("slow",0.15);
        $(".div2").fadeTo("slow",0.5);
        $(".div3").fadeTo("slow",0.7);
    });

    // 滑动
    var $button = $(".box5>button");
    var $box = $(".box4");
    $button.first().click(function () {
        $box.slideDown("slow");
    });
    $button.eq(1).click(function () {
        $box.slideUp("slow");
    });
    $button.eq(2).click(function () {
        $box.slideToggle("slow");
    });

    // animate:自定义动画
    var $button = $(".box6>button");
    $button.first().click(function () {
        $box.animate({height:"300px"}).delay(5000); // 延迟5s后再发生下一个动画
    });
    $button.eq(1).click(function () {
        $box.animate({height:"200px"});
    });
</script>
```

## 九、json数据类型

### 9.1 json对象

var user = {"name" : "summer" ,"age":18}

### 9.2 json读

user.name

user.age

### 9.3 json写

user.name="summer1"

### 9.4 json 数据遍历

for(var ket in user){

​	key+":"+user[key]

}

### 9.5 json转字符串

var str = JSON.stringify(user);

### 9.6 字符串转json

var obj = JSON.parse(str);

```
<script>
    // json数据类型
    // json对象
    var user={
        "name": "feifei",
        "age":18,
        "sex": "female"
    };
    // json读
    console.log(user.name);
    console.log(user.age);
    // json写
    user.name="邱子宸";
    console.log(user.name);
    // json数据遍历
    for(var key in user){
        console.log(key+":"+user[key]);
    }
    // json转字符串
    var str = JSON.stringify(user);
    console.log(str);
    console.log(typeof str);

    // 字符串转json
    var obj = JSON.parse(str);
    console.log(obj);
    console.log(typeof obj);
</script>
```

## 十、form前后台交互

**lable标签的for指向后面内部的id值**

**form表单有一个属性，action表示提交的地址。需要在action里添加后台的路由地址。**

```
<body>
    <form action="/login" method="post">
        <p><label for="user">用户名:</label><input type="text" name="user" id="user" placeholder="请输入用户名"></p>
        <p><label for="psw">密&emsp;码:</label><input type="password" name="psw" id="psw" placeholder="请输入密码"></p>
        <p><input type="submit" value="登录"></p>
    </form>
</body>
```

### 后台

登录的路径：

127.0.0.1:8888/login
**/login这个为他的路由**

在tornado.web.Application([
        (r"/login", MainHandler),
    ])这里设置。

#### 页面渲染

self.render("login.html")



#### 拿参

self.get_argument

```
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("login.html")

    def post(self):
        print(self.get_argument("user"))
        print(self.get_argument("psw"))
        self.write("登录成功")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/login", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

