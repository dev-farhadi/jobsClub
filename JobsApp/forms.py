from django import forms
from django.contrib.auth.forms import UserCreationForm
from JobsApp.models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password1', 'password2')