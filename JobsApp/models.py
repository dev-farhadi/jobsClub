from django.db import models
from django.conf import settings

class Employer(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255, default='N/A')
    co = models.CharField(max_length=255, default="N/A")

    def __str__(self):
        return str(self.co)
    
class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    employer = models.ForeignKey('Employer',on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='N/A')
    description = models.TextField(max_length=1080)


    def __str__(self):
        return str(self.id)
    
    
class JobsUser(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
