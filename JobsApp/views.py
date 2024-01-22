from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
     form = UserCreationForm(request.POST)

     if form.is_valid():
       user = form.save()
       login(request, user)
       return HttpResponse('user created!')

    form = UserCreationForm()
    return render(request, 'signup.html', {'form' : form})

def loginView(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
          user = form.get_user()
          login(request, user)
          return redirect('home')

    else:
     form = AuthenticationForm()
     return render(request, 'login.html', {'form' : form})

def logoutView(request):
   if request.method == 'POST':
      logout(request)
      return redirect('home')
   

def homeView(request):
    return render(request, 'home.html')

