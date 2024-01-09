from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def landing(request):
    return render(request, "login/Login.html")

def login(request):
    if request.method == "POST":
        ID = request.POST['id']
        PW = request.POST['pw']
        user = auth.authenticate(request, username=ID, password=PW)
        if user is not None:
            auth.login(request, user)
            return redirect('/Board/')
        else:
            return render(request, 'login/Login.html')
    else:
        return render(request, 'login/Login.html')

def logout(request):
    auth.logout(request)
    return render(request, "login/Login.html")

def Sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2'] and len(request.POST['username']) > 0:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/Board/')
    return render(request, 'login/Login.html')