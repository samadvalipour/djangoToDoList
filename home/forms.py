from dataclasses import fields
from tkinter import Label
from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField(label="عنوان",required=True)
    body = forms.CharField(label="توضیحات",required=True)
    done = forms.BooleanField(label="انجام شده",required=False)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","body","done"]
        labels = {"title":"عنوان","body":"توضیحات","done":"انجام شده"}