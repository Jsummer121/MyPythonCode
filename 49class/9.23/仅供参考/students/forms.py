from django import forms
from students.models import Student, StudentDetail


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student     # 模型
        # fields = '__all__'  # 字段
        exclude = ['is_delete']  # 排除字段
        # widgets = {
        #     'sex': forms.RadioSelect()
        # }

    def clean_phone(self):  # 指定字段校验
        phone = self.cleaned_data.get('phone')
        if phone == '13055556666':
            raise forms.ValidationError('手机号码已经注册，请重新输入！')
        return phone


class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail     # 模型
        exclude = ['student']   # 关联字段不需要展示


