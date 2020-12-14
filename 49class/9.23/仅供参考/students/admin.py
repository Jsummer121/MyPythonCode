from django.contrib import admin
from .models import Student, StudentDetail
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'qq', 'phone']
    list_display_links = ['name', 'sex']
    list_filter = ['sex']
    search_fields = ['name', 'qq', 'phone']
    list_per_page = 5

    # 详情页
    # fields = ['age', 'qq']
    fieldsets = [   # 分组设置
        (None, {'fields': ['name', 'sex']}),
        ('详细信息', {'fields': ['qq', 'phone', 'grade']}),
        ('设置', {'fields': ['is_delete']}),

    ]

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail)
