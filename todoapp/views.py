from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.shortcuts import render,get_object_or_404

# Create your views here.

@login_required(login_url = "/accounts/login/")
def home(request):
    tasks = Task.objects.all().order_by('priority').filter(owner = request.user)
    # print(request.user,"AuthUser!!!!!!!")
    return render(request,'index.html',{'tasks':tasks})

def taskDelete(request,task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return redirect('/')

def add_task(request):
    name = request.POST["task_name"]
    priority = request.POST["task_priority"]
    user_name = request.POST.get('username')
    print(user_name,"USERRRR!!")
    user = get_object_or_404(User,username = user_name)
    task = Task(name = name,priority = priority,owner = user )
    task.save()
    return redirect("/")

def taskComplete(request,task_id):
    task = Task.objects.get(id = task_id)
    if task.complete == True:
        task.complete = False
    else:
        task.complete = True
    task.save()
    return redirect("/")


# use the URL 'cvbtask/' to get the class based view below
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'