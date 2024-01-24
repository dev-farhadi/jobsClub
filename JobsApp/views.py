from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Jobs,JobsUser, JobCategory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

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
      return redirect('login')
   

def homeView(request):
    
    jobs = Jobs.objects.order_by('-id')[:5]
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

@login_required
def applyView(request, jj):
   d = JobsUser.objects.filter(job_id=jj, user_id=request.user.id).exists()
   job = Jobs.objects.get(id=jj)
   user = User.objects.get(id=request.user.id)
   instance = JobsUser(job_id=job, user_id=user)
   instance.save()
   return render(request, 'apply.html', {'d': d})


def jobsView(request):

   if request.method == 'POST':
      selected = request.POST.get('selected_option')
      jobs = Jobs.objects.filter(category__cat=selected)
      paginator = Paginator(jobs, 5)
      page_number = request.GET.get("page")
      page_obj = paginator.get_page(page_number)
      opt = JobCategory.objects.all()
      return render(request, 'jobs.html', {'page_obj' : page_obj, 'opt' : opt, 'selected' : selected})
   else:
    jobs = Jobs.objects.all()
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    opt = JobCategory.objects.all()
    return render(request, 'jobs.html', {'page_obj' : page_obj, 'opt' : opt})

def job(request,jv):
   job = Jobs.objects.filter(id=jv)
   return render(request, "job.html", {'job' : job})
