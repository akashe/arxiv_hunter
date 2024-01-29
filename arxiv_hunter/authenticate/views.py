from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request=request, template_name="authenticate/home.html", context={})

def login_user(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message=("Login Successfull!!!"))
            return redirect(to="home")
        else: 
            messages.error(request=request, message=("Login Error. Try again..."))
            return redirect(to="login_user")
    else:
        return render(request=request, template_name="authenticate/login.html", context={})
    
def logout_user(request):
    logout(request=request)
    messages.success(request=request, message=("LogOut Successfull!!!"))
    return redirect(to="home")

def signup_user(request):
    if request.method == 'POST':
        pass
        # username=request.POST["username"]
        # password=request.POST["password"]
        # user=authenticate(request=request, username=username, password=password)
        # if user is not None:
        #     login(request=request, user=user)
        #     return redirect(to="home")
        # else: 
        #     return redirect(to="login_user")
    else:
        return render(request=request, template_name="authenticate/signup.html", context={})
