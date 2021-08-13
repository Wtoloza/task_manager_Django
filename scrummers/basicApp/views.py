from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Task
from .models import Project

from .form import TaskForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def app(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    context = {
        'task':tasks,
        'project': projects
    }
    print(context)
    return render(request, 'app.html', context)

def createTask(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        tasks = Task.objects.all()
        form = TaskForm
        context = {
        'form':form,
        'project': projects,
        'task':tasks,
        }
        return render(request, 'createTask.html', context)
    else:
        title_task = request.POST['txtTitleTask']
        project_task = request.POST['txtProject']
        imporant_task = request.POST['numImportance']

        task = Task(
            title_task=title_task,
            project_task=Project(project_task),
            imporant_task=imporant_task
        )
        task.save()
        return redirect('/')


def createProject(request):
    if request.method == 'POST':
        id_project = request.POST['idProject']
        name_project = request.POST['nameProject']

        project = Project(
            id_project=id_project,
            name_project=name_project
        )
        project.save()
        return redirect('/')

    else:
     return redirect('/')

def functions(request):
    if request.method == 'POST':
        id_task = request.POST['idTask']
        btn = request.POST['btn']

        if btn == 'Edit':
            print(btn)
        elif btn == 'Delete':
            try:
                task = Task.objects.get(id_task=id_task)
                task.delete()
                return redirect('/')  
            except:
                return redirect('/')                
            
        elif btn == 'Check':
            try:
                task = Task.objects.get(id_task=id_task)
                task.status_task = True
                task.save()
                return redirect('/')  
            except:
                return redirect('/')

    else:
     return redirect('/')