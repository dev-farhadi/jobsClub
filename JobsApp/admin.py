from django.contrib import admin
from .models import Jobs, JobsUser, Employer
# Register your models here.
admin.site.register(Jobs)
admin.site.register(JobsUser)
admin.site.register(Employer)


