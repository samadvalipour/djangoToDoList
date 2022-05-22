from cProfile import label
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    email = forms.EmailField(label="ایمیل")
    password = forms.CharField(label="رمز عبور")

class LoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(label="رمز عبور")