// 轮播图
$(function () {
    // 获取操作对象
    var $pic = $(".pic li img"), // 图片对象
        $btn = $(".btn li"), // 小圆点对象
        $tab = $(".tab li"), // 左右箭头
        $banner = $(".banner"); // div对象
    var n=1;// 定义一个变量，指向当前显示的图片的下标
    // 初始化
    $pic.eq(n).addClass("show");
    $btn.eq(n).addClass("active");

    // 小圆点的点击事件
    $btn.click(function () {
        // console.log($(this).index());
        var num = $(this).index();// 点击对象的下标
        if(num!=n){ // 优化：当点击对象和当前对象重复时，功能不执行
            change(num);
        }
    });
    
    // 优化：图片和小圆点切换功能封装成函数
    function change(num){
        $pic.eq(n).fadeOut(2000);
        $btn.eq(n).removeClass("active");
        n = num;
        $pic.eq(n).fadeIn(2000);
        $btn.eq(n).addClass("active");
    }
    // 左右箭头
    $tab.click(function () {
        var num = n; // 获取当前显示的对象序列
        // console.log($(this).index()); // 0左箭头1右箭头
        if($(this).index()){// 右箭头
            num++;
            // 0,1,2,3,4,5,6,7,8
            // %4
            // 0,1,2,3,0,1,2,3,0
            num%=$pic.length;
        }else{// 左箭头
            num--;
            if(num <0){
                num = $pic.length-1;
            }
        }
        change(num);
    });

    // 自动轮播
    function f(){
        var num =n;// 获取当前显示的对象序列
        num++;
        // 0,1,2,3,4,5,6,7,8
        // %4
        // 0,1,2,3,0,1,2,3,0
        num%=$pic.length;
        change(num);
    }
    var SI = setInterval(f, 5000);
    $banner.hover(function () {
        clearInterval(SI);
    },function () {
        SI = setInterval(f, 5000);
    });
});