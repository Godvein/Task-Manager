from django.urls import path
from tasks import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('addtasks/', views.addTasks, name = "addtasks"),
    path('tasks/', views.viewTasks, name = "tasks"),
    path('completetasks/<id>/', views.completeTasks, name = "completetasks"),
    path('deletetasks/<id>/', views.deleteTasks, name = "deletetasks"),
    path('edit/<id>/', views.editTask, name = "edittask"),
    path('logout/', views.logOut, name = "logout")
]