"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/guangtouqiang/', views.index, name='index'),
    # path('detail/<id>/<int:year>/<int:month>/', views.detail),
    re_path(r'detail/(?P<id>\d+)/(?P<year>\d{4})/(?P<month>[0-9]|1[0-2])/', views.detail),
    path("student/<name>/", views.student, kwargs={'name': '邱子宸'}),
    path("test1/", views.test1),
    path("login/", views.login),
    # path("teacher/", include('teacher.urls')),
    # path("teacher/<name>/", include('teacher.urls')),   # 参数会传递到include下面包含的每一个路径中，这种要谨慎使用
    # path("", include('teacher.urls'), kwargs={"name": "张博文"}),
    path("teacher/", include("teacher.urls")),
    path("students/", include("students.urls")),
]
