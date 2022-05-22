from turtle import title
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm

def home(request):
    all = Todo.objects.all()
    return render(request,"home.html",{'title':'home','todos':all})

def detail(request,todo_id):
    todo = Todo.objects.get(id =todo_id)
    return render(request,"detail.html",{"title":"home","todo":todo})

def delete(request,todo_id):
    todo = Todo.objects.get(id =todo_id).delete()
    messages.success(request,"حذف با موفقیت انجام شد","success")
    return redirect('home')

def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,"با موفقیت بروز رسانی شد","success")
            return redirect('home')
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request,'update.html',{'form':form})
        
def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            Todo.objects.create(title=form.cleaned_data['title'],body=form.cleaned_data['body'],done=form.cleaned_data['done'])
            messages.success(request,"با موفقیت افزوده شد","success")
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request,'create.html',{'form':form})