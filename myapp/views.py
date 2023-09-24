from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404
from .forms import CreateNewTask


# Create your views here.
def index(request):
    title = 'welcome to the django course!!'
    return render(request, 'index.html', {
        'titulo': title
    })

def intro(request, username):
    return HttpResponse("<h1>mi primer linea en django con %s<h1>" % username)

def hello(request, id):
    result = id + 100 * 3
    return HttpResponse("<h1>Hello, este es el resultado de la operacion %s<h1>" % result)

def about(request):
    username = 'juan'
    return render(request, 'about.html', {
        'user' : username
    })
    
def projects(request):
    # projects = list(Project.objects.values())
    project1 = Project.objects.all()
    return render(request, 'project.html', {
        'projects': project1
    })
    
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tareas' : tasks
    })  

def create_task(request):
    print(request.GET['title'])
    print(request.GET['description'])
    Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id2=2),
    return render(request, 'create_task.html',{
        'formulario': CreateNewTask
    })