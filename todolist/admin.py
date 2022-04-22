from django.contrib import admin

from .models import Todolist # .models means importing models from current directory(todolist) import the Todolist model
# Register your models here.

admin.site.register(Todolist)
