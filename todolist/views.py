
from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    # for querying all items in DB that match TodoList and order them by id
    todo_items = Todolist.objects.order_by('id')
    # instantiate form 
    form = TodoListForm()
    # The actual todo_items iss returened from above and passed to context , this context will get passed to template and this template will have access to DB
    context = {'todo_items' : todo_items, 'form' : form} # add the form to context sso that we have access to it in template
    #this would return the index.html from the temlplates folder 
    return render(request, 'todolist/index.html', context) 
# for above function to work we need to map it in url pattern

# Below function is to caputre the dat through form and save it as DB object in table using POST method
@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    

    return redirect('index')

def completedTodo(request, todo_id):  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')



