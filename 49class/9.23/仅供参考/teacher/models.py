from django.db import models


# Create your models here.
class Student(models.Model):
    num = models.AutoField(primary_key=True)  # 如果不指定自动生成
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    height = models.IntegerField(null=True)
    sex = models.SmallIntegerField(default=1)   # 设置默认值
    qq = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    # c_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)    # auto_now_add=True
    c_time = models.DateTimeField("创建时间", auto_now_add=True)    # auto_now_add=True自动填充当前时间
    x_time = models.DateTimeField("修改时间", auto_now=True)

    def __str__(self):
        return self.name
