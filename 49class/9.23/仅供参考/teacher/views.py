from datetime import datetime
import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from django.urls import reverse

from teacher.models import Student
from CRM.settings import MEDIA_ROOT
from teacher.forms import RegisterForm


def students(request, name):
    return HttpResponse("{}成功".format(name))


def test1(request):
    name = "小广"
    # return HttpResponse('<h1 style="color:red">我是前端代码</h1>')    # 硬编码
    # t = get_template('teacher/test.html')
    # html = t.render()
    # return HttpResponse(html)
    return render(request, 'teacher/test.html', context={
        'name': name,
    })


def index(request):
    num = request.COOKIES.get('num.txt')
    if num:
        num = int(num) + 1
    else:
       num = 1

    now = datetime.now()    # 获取当前时间 utc时间
    # now = now.strftime('%Y年%m月%d日 %H：%M：%S')  # datetime下时间格式
    date_format = "Y年m月d日 H：i:s"    # django下的时间格式
    format_str = '%Y年%m月%d日 %H：%M：%S'
    lt = [4, 5, 6]
    dt = {"name": "戴震飞", "age": 18, "height": 182}
    st = "hello,TZ"
    js = "<script>alert('1')</script>"
    # sts = [
    #     {"name": "戴震飞", "age": 18, "height": 182, 'sex': 1, 'course': ['python', 'java', 'c++', 'web前端']},
    #     {"name": "翁国伟", "age": 15, "height": 185, 'sex': 1, 'course': ['python', 'java', 'c++', 'web前端']},
    #     {"name": "黄夕", "age": 18, "height": 182, 'sex': 1, 'course': ['python', 'java', 'c++', 'web前端']},
    #     {"name": "朦胧", "age": 18, "height": 182, 'sex': 0, 'course': ['python', 'java', 'c++', 'web前端']},
    # ]
    sts = Student.objects.all()
    response = render(request, "teacher/index.html", context={
        "num.txt": num,
        "now": now,
        "lt": lt,
        "dt": dt,
        "st": st,
        "date_format": date_format,
        "js": js,
        "students": sts,
        'format_str': format_str,
    })
    response.set_cookie('num.txt', num, max_age=5)  # 设置cookie有效值， 5秒后重置
    return response


def login(request):
    if request.method == 'POST':
        # file = request.FILES.get('file')    # 上传一个文件
        files = request.FILES.getlist('file')   # 上传多个文件

        # 每天的文件放到每天的文件夹
        day_dir = datetime.now().strftime('%Y%m%d')
        dir_path = os.path.join(MEDIA_ROOT, day_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        for file in files:
            filename = os.path.join(dir_path, file.name)
            with open(filename, 'wb')as f:
                for line in file.chunks():  # 上传文件过大时
                    f.write(line)

    # if request.method == 'GET':
    #     return render(request, "teacher/login.html")
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     if username == 'fei' and password == 'fei':
    #         return redirect('teacher:index')
    #     # else:
    #     #     return render(request, "teacher/login.html")
    return render(request, "teacher/login.html")


def detail(request, name):
    return HttpResponse("{}同学的详情".format(name))


def test_json(request):
    sex = request.GET.get('sex')
    sex = int(sex)
    res = Student.objects.values('name', 'age', 'sex').filter(sex=sex)
    res = list(res)
    data = {'result': res}
    return JsonResponse(data)


def register(request):
    if request.method == 'GET':
        form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)   # 实例化对象，此时的对象有了你填入的数据

        if form.is_valid():  # 字段校验，校验成功返回True
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                return HttpResponse('注册成功')

    return render(request, 'teacher/register.html', context={
        'form': form,
    })
