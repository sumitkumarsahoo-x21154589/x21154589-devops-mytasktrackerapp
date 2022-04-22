# This file will be used to redirect to different views as per the endpoint added to the url
from django.urls import path
from . import views # here '.' dot means from current directory

urlpatterns = [
    path('', views.index, name='index'), # here while hitting the url without end point it will redirect to index.html which i have created as function inside views.py
    path('add', views.addTodoItem, name='add'), # the name here is use for referencing it to template for adding tasks
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]