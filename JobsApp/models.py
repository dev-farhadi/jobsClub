from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class EmployerEntity(models.Model):
    id = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=255)    

    def __str__(self):
        return str(self.cat)
    

class Employer(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255, default='N/A')
    co = models.CharField(max_length=255, default="N/A")
    category = models.ForeignKey(EmployerEntity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.co)
    
class JobCategory(models.Model):
    id = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=255)

    def __str__(self):
        return str(self.cat)    
    
class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    employer = models.ForeignKey('Employer',on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='N/A')
    description = models.TextField(max_length=1080)

    def __str__(self):
        return str(self.category)
    
    
class JobsUser(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-details', args=[str(self.id)])
