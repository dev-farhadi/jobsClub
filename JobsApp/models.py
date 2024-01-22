from django.db import models

class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(max_length=1080)


    def __str__(self):
        return str(self.id)