from django.urls import path
from .views import signup, loginView, homeView, logoutView, applyView

urlpatterns = [

   path('<int:jj>/', applyView, name="apply"),
   path('home/', homeView, name="home"),
   path('signup/', signup, name="signup"),
   path('login/', loginView, name="login"),
   path('logout/', logoutView, name="logout")
]
