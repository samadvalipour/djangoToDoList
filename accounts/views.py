from turtle import home
from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd["username"],cd["email"],cd["password"])
            messages.success(request,"ثبت نام با موفقیت انجام شد","success")
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request,"register.html",context={"form":form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request,"کاربر گرامی خوش امدید","success")
                return redirect("home")
            else:
                messages.error(request,"کاربری با اطلاعات وارد شده موجود نمی باشد","danger")
                return render(request,"login.html",context={"form":form})

    else:
        form = LoginForm()
        return render(request,"login.html",context={"form":form})

def user_logout(request):
    logout(request)
    messages.warning(request,"شما از سیستم خارج شدید","warning")
    return redirect("home")