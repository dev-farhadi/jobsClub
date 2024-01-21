from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
  template = loader.get_template('home.html')

  return HttpResponse(template.render())

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]     
    user = authenticate(request, username=username, password=password)
   
    if user is not None:
      login(request, user)
      return redirect('home')

