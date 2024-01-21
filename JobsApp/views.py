from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.template import loader

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
   if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']

      if User.objects.filter(username=username, password=password).exists():
         return redirect('home')
      else:
        template = loader.get_template('login.html')
        context = {
           'error' : 'username or password wrong!',
           'asdasd' : 'asdasdasd'
        }
        return HttpResponse(template.render(context, request))
      
   return render(request, 'login.html')   
   

