from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username, email, password)
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "register.html")

        # Validate email format (basic check)
        if "@" not in email or "." not in email:
            messages.error(request, "Invalid email format.")
            return render(request, "register.html")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("/home/")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            messages.error(request, "All fields are required.")
            return render(request, "login.html")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
        else:
            messages.error(request, "error loging in")

    return render(request, "login.html")
