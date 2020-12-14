from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Student, Grade, StudentDetail
from .forms import StudentForm

# Create your views here.
def student_list(request):
    section = "学生列表"

    # 查询功能
    search = request.GET.get("search", "").strip()

    if search:
        if search.isdigit():
            sts = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
        else:
            sts = Student.objects.filter(name=search, is_delete=False)
    else:
        sts = Student.objects.filter(is_delete=False)

    sts = sts.order_by('-c_time')   # 排序

    # 实现分页
    # 数据总量
    total_num = sts.count()
    # 每页数据条数
    per_page = request.GET.get('per_page', 10)
    # 当前页码
    page = request.GET.get('page', 1)

    paginator = Paginator(sts, per_page)
    sts = paginator.get_page(page)
    total_page = paginator.num_pages

    return render(request, 'students/student_list.html', context={
        "section": section,
        "search": search,
        "students": sts,
        "per_page": per_page,
        "total_page": total_page,
        "page": page,
    })


def student_detail(request, pk):
    section = "学生详情"
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', context={
        "section": section,
        "student": student,
    })


def student_add(request):
    section = "添加学生"
    if request.method == 'GET':
        return render(request, 'students/student_detail.html', context={
            'section': section,
        })

    if request.method == 'POST':
        # 接收传送过来的数据，并保存到数据库
        # 1.获取学生信息
        data = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'sex': request.POST.get('sex'),
            'qq': request.POST.get('qq'),
            'phone': request.POST.get('phone'),
            'grade_id': request.POST.get('grade'),
        }
        student = Student.objects.create(**data)

        # 2.获取学生详情并保存数据库
        StudentDetail.objects.create(
            college=request.POST.get('college'),
            student=student  # 表关联
        )
        return redirect("student:student_list")


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.is_delete = True
    student.save()
    return redirect("student:student_list")


def student_edit(request, pk):
    section = "学生信息修改"
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'students/student_detail.html', context={
            "section": section,
            "student": student,
        })

    if request.method == 'POST':
        # 学生列表
        grade_id = request.POST.get('grade')
        try:
            grade = Grade.objects.get(pk=grade_id)
        except:
            grade = None

        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.sex = request.POST.get('sex')
        student.qq = request.POST.get('qq')
        student.phone = request.POST.get('phone')
        student.grade = grade  # 表关联

        # 学生详情
        try:
            student_detail = student.studentdetail  # 反向
        except:
            student_detail = StudentDetail()    # 正向
            student_detail.student = student    # 表关联

        student_detail.college = request.POST.get('college')

        student_detail.save()
        student.save()

        return redirect('student:student_list')


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password')
        if username == 'fei' and password == 'fei':
            request.session['name'] = username
            request.session.set_expiry(5)  # 设置过期时间，10秒后重置
            return redirect("student:index")

    return render(request, "students/login.html")


def index(request):
    name = request.session.get('name', '游客')
    return render(request, 'students/index.html', context={
        "name": name
    })


def logout(request):
    request.session.flush()
    return redirect('student:index')


def detail_form(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    return render(request, 'students/detail_form.html', context={
        'form': form,
    })
