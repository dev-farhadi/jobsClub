from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.template import loader
import time

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        family = request.POST['family']
        username = request.POST['username']
        password = request.POST['password']

        user = User(username=username, password=password, name=name, family=family)
        user.save()
        return redirect('success') # Redirect to a success page   

    return render(request, 'signup.html')

def success(request):
  template = loader.get_template('success.html')
 #time.sleep(3)
  #return redirect('signup')

  return HttpResponse(template.render())

# Create your views here.
