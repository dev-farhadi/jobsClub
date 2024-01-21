from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        family = request.POST['family']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
           template= loader.get_template('signup.html')
           context = {
              'error': 'Username Exist!'
           }
           return HttpResponse(template.render(context, request))
        else:
         user = User(username=username, password=password, name=name, family=family)
         user.save()
         return redirect('login') # Redirect to a login page   

    return render(request, 'signup.html')

def home(request):
  template = loader.get_template('home.html')

  return HttpResponse(template.render())

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]

    if User.objects.filter(username=username, password=password).exists():  
      
      user = authenticate(request, username=username, password=password)
   
      if user is not None:
        login(request, user)
        return redirect('home')
    else:
       template = loader.get_template('login.html')  
       context = {
              'error': 'Username or password is wrong!'
           }
    return HttpResponse(template.render(context, request))
