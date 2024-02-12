from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'authentication\index.html')
def SignUp(request):
    if request.method == "post":
        name1 = request.post.get('name1')
        name2 = request.post.get('name2')
        email = request.post.get('email1')
        email2 = request.post.get('email2')
        pass1 = request.post.get('pass1')
        pass2 = request.post.get('pass2')

    user = user.objects.create_user(name1, email, pass1)
    user.first_name = name1
    user.last_name = name2
    user.save()

    messages.success(request, "Your account has been created successfully")

    return redirect('Login')

    return render(request, 'authentication\SignUp.html')
def Login(request):
    return render(request, 'authentication\Login.html')

    if request.method == "post":
        email = request.post.get('email1')
        pass1 = request.post.get('pass1')
    user = authenticate(name1, email, pass1)
    if user is not None: 
        login(request, user)
    else:
        messages.error(request, "Email and Password do not match")
    
def SignOut(request):
    return render(request, 'authentication\SignOut.html')