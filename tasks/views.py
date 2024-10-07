from django.shortcuts import render,redirect, get_object_or_404
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url="/login/")
def home(request):
   taskmodel = Tasks.objects.filter(user = request.user).count()
   numdict = {
      "taskmodel" : taskmodel
   }
   return render(request, "index.html", numdict)

@login_required(login_url="/login/")
def addTasks(request):
   if request.method == "POST":
      name = request.POST.get("name")
      description = request.POST.get("description")
      query = Tasks(user = request.user, name = name, description = description)
      query.save()
   return render(request, "addtasks.html")

@login_required(login_url="/login/")
def viewTasks(request):
   taskmodel = Tasks.objects.filter(user=request.user)
   alltasks = {
      "tasks" : taskmodel
   }
   return render(request, "tasks.html", alltasks)

@login_required(login_url="/login/")
def completeTasks(request, id):
   taskmodel = get_object_or_404(Tasks, id=id, user=request.user)
   taskmodel.delete()
   messages.success(request, "Congratulations on completing the task: " + taskmodel.name)
   return redirect("/tasks/")

@login_required(login_url="/login/")
def deleteTasks(request, id):
   taskmodel = get_object_or_404(Tasks, id=id, user=request.user)
   taskmodel.delete()
   return redirect("/tasks/")

@login_required(login_url="/login/")
def editTask(request, id):
   taskmodel = get_object_or_404(Tasks, id=id, user=request.user)
   task = {
      "taskmodel" : taskmodel
   }
   if request.method == "POST":
      taskmodel.name = request.POST.get("name")
      taskmodel.description = request.POST.get("description")
      taskmodel.save()
      return redirect("/tasks/")
   return render(request, "edittask.html", task)

def logOut(request):
   logout(request)
   return redirect("login")
