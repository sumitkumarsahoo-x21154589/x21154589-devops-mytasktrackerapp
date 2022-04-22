
from django.shortcuts import render
from .models import Todolist
# Create your views here.

def index(request):
    # for querying all items in DB that match TodoList and order them by id
    todo_items = Todolist.objects.order_by('id') 
    # The actual todo_items iss returened from above and passed to context , this context will get passed to template and this template will have access to DB
    context = {'todo_items' : todo_items}
    #this would return the index.html from the temlplates folder 
    return render(request, 'todolist/index.html', context) 
# for above function to work we need to map it in url pattern