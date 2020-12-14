from django import forms
from students.models import Student, StudentDetail


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student     # 模型
        fields = '__all__'

# class StudentDetailForm(forms.ModelForm):
#     class META:
#         model = StudentDetail     # 模型


