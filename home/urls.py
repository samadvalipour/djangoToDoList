from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<todo_id>',views.detail,name='detail'),
    path('delete/<todo_id>',views.delete,name='delete'),
    path('create/',views.create,name='create'),
    path('update/<todo_id>',views.update,name='update'),

]
