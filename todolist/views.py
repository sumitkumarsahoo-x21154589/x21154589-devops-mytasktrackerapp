from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'todolist/index.html') #this would return the index.html from the temlplates folder 
# for above function to work we need to mao it in url pattern