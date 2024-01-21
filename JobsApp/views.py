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
              'error': 'bad bad'
           }
           return HttpResponse(template.render(context, request))
        else:
         user = User(username=username, password=password, name=name, family=family)
         user.save()
         return redirect('home') # Redirect to a success page   

    return render(request, 'signup.html')

def home(request):
  template = loader.get_template('home.html')

  return HttpResponse(template.render())
   

# Create your views here.
