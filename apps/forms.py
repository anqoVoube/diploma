from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.utils import timezone

from .models import Employee, Department, Kin, Attendance, Leave, Recruitment


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph', required=True,
                             widget=forms.FileInput(attrs={'class': 'form-control mt-2'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'thumb')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username Here', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))


class EmployeeForm(forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(strip=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
                                 label='Имя')
    last_name = forms.CharField(strip=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
                                label='Фамилия')
    mobile = forms.CharField(strip=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Мобильный телефон'}),
                             label='Мобильный телефон')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}),
        label='Электронная почта')
    emergency = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Срочный контакт'}),
        label='Срочный контакт')
    gender = forms.ChoiceField(choices=Employee.GENDER, widget=forms.Select(attrs={'class': 'form-control'}),
                               label='Пол')
    department = forms.ModelChoiceField(Department.objects.all(), required=True, empty_label='Select a department',
                                        widget=forms.Select(attrs={'class': 'form-control'}), label='Отдел')
    language = forms.ChoiceField(choices=Employee.LANGUAGE, widget=forms.Select(attrs={'class': 'form-control'}),
                                 label='Язык')

    class Meta:
        model = Employee
        fields = (
            'first_name', 'last_name', 'mobile', 'email', 'emergency', 'salary', 'gender', 'department', 'bank',
            'nuban',
            'language', 'thumb')
        widgets = {
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'nuban': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'salary': 'Зарплата',
            'bank': 'Банк',
            'nuban': 'Номер счета',
            'thumb': 'Фото'
        }


class KinForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Адрес')
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Работа')
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Мобильный телефон')
    employee = forms.ModelChoiceField(Employee.objects.filter(kin__employee=None), required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Сотрудник')

    class Meta:
        model = Kin
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название отдела'}),
                           label='Название')
    history = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Краткая история кафедры'}), label='История')

    class Meta:
        model = Department
        fields = '__all__'


class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS, widget=forms.Select(attrs={'class': 'form-control w-50'}))
    staff = forms.ModelChoiceField(
        Employee.objects.filter(Q(attendance__status=None) | ~Q(attendance__date=timezone.localdate())),
        widget=forms.Select(attrs={'class': 'form-control w-50'}))

    class Meta:
        model = Attendance
        fields = ['status', 'staff']


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

        widgets = {
            'start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'position': 'Должность',
            'email': 'Электронная почта',
            'phone': 'Телефон',
        }
