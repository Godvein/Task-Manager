from django.shortcuts import render,redirect
from .models import Tasks
from django.contrib import messages
# Create your views here.
def home(request):
   taskmodel = Tasks.objects.count()
   numdict = {
      "taskmodel" : taskmodel
   }
   return render(request, "index.html", numdict)

def addTasks(request):
   if request.method == "POST":
      name = request.POST.get("name")
      description = request.POST.get("description")
      query = Tasks(name = name, description = description)
      query.save()
   return render(request, "addtasks.html")

def viewTasks(request):
   taskmodel = Tasks.objects.all()
   alltasks = {
      "tasks" : taskmodel
   }
   return render(request, "tasks.html", alltasks)

def completeTasks(request, id):
   taskmodel = Tasks.objects.get(id = id)
   taskmodel.delete()
   messages.success(request, "Congratulations on completing the task: " + taskmodel.name)
   return redirect("/tasks/")

def deleteTasks(request, id):
   taskmodel = Tasks.objects.get(id = id)
   taskmodel.delete()
   return redirect("/tasks/")

def editTask(request, id):
   taskmodel = Tasks.objects.get(id = id)
   task = {
      "taskmodel" : taskmodel
   }
   if request.method == "POST":
      taskmodel.name = request.POST.get("name")
      taskmodel.description = request.POST.get("description")
      taskmodel.save()
      return redirect("/tasks/")
   return render(request, "edittask.html", task)
