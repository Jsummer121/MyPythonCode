from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse("主页")


def login(request):
    return redirect("student:index")    # app_name:name


def test2(request):
    return render(request, "test2.html")
