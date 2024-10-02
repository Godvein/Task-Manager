from django.shortcuts import render
from .models import Tasks
# Create your views here.
def home(request):
   return render(request, "index.html")

def addTasks(request):
   if request.method == "POST":
      name = request.POST.get("name")
      description = request.POST.get("description")
      query = Tasks(name = name, description = description)
      query.save()
   return render(request, "addtasks.html")