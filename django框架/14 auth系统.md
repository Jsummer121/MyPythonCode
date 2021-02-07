[TOC]

### 权限系统

django文档：https://docs.djangoproject.com/en/2.1/topics/auth/

```
django自带的用户身份验证系统：
1.用户验证：登录的账号是否是真正的用户
2.授权：允许用户做什么
```

#### 一、用户验证

##### 1.1 实现登录

```
# views.py

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    # user = request.user
    # 判断是否登录
    if request.user.is_authenticated:   # 匿名用户返回false
        return redirect("student:student_list")

    if request.method == 'POST':
        # 获取用户名密码
        username = request.POST.get('username')
        password = request.POST['password']
        # 校验用户名密码
        user = authenticate(username=username, password=password)   # 正确返回user对象，错误返回None
        if user is not None:
            # 用户信息存放到session并登录
            login(request, user)
            return redirect("student:student_list")

    return render(request, "students/login.html")
```

```
# login.html
<body>
    欢迎{{ user.username|default:'游客' }}访问

    {% if user.is_authenticated %}
    <a href="{% url "student:logout" %}">退出</a>
    {% else %}
     <a href="{% url "student:login" %}">登录</a>
    {% endif %}
</body>
```

##### 1.2 实现退出

```
def logout_view(request):
    logout(request)
    return redirect('student:index')
```

##### 1.3 实现限制

```
def student_list(request):
    # 限制登录
    if not request.user.is_authenticated:   # 未登录用户访问，返回登录页面
        return redirect('student:login')
    .....    
```

##### 1.4 限制优化

```
# 登录优化一：实际开发过程中，如果我要访问某个页面，而这个页面需要登录权限，我们登录后自动跳转回此前我想访问的页面。
处理方式，把当前的路径当做参数传入
# 登录优化二：多个视图函数，同时需要添加这个功能，需要在每个视图都加上相同的内容，代码冗余
处理方式：装饰器

@login_required
def student_list(request):
    # # 限制登录
    # if not request.user.is_authenticated:   # 未登录用户访问，返回登录页面
    #     return redirect(reverse('student:login') + '?next={}'.format(request.path_info))
    #     # student/login/?next="student/student_list/"
    
# settings.py
from django.urls import reverse, reverse_lazy

LOGIN_URL = reverse_lazy('student:login')    
```

#### 二、授权

