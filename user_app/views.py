from django.contrib.auth import authenticate, login, logout
from user_app.forms import RegisterForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user  = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username or password is invalid")

    return render(request, "user_app/login.html")

def Register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect("login")
    context = {"form": form}
    return render(request, "user_app/register.html", context)

def Logout(request):
    logout(request)
    return redirect("home")

def Dashboard(request):
    return render(request, 'user_app/main_dashboard.html')