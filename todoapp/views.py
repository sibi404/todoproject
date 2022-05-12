from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.views.generic import ListView

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})

def taskDone(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/')

def add_task(request):
    name = request.POST["task_name"]
    priority = request.POST["task_priority"]
    task = Task(name = name,priority = priority)
    task.save()
    return redirect("/")

# use the URL 'cvbtask/' to get the class based view below
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'