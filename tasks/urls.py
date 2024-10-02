from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('addtasks/', views.addTasks, name = "addtasks")
]