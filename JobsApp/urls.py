from django.urls import path
from .views import signup, loginView, homeView, logoutView, applyView, jobsView, job, blog_list, blog_detail

urlpatterns = [
      path('blogs/', blog_list, name='blog-list'),
    path('blogs/<int:pk>/', blog_detail, name='blog-detail'),
   path('job/<int:jv>', job, name="job"),
   path('<int:jj>/', applyView, name="apply"),
   path('jobs/', jobsView, name="jobs"),
   path('home/', homeView, name="home"),
   path('signup/', signup, name="signup"),
   path('login/', loginView, name="login"),
   path('logout/', logoutView, name="logout")
]
