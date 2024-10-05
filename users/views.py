from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        
        email = request.POST.get("email")
        if email is None:
            return render(request, "register.html")
        password = request.POST.get("password")
        if password is None:
            return render(request, "register.html")
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("/home/")
    return render(request, "register.html")
