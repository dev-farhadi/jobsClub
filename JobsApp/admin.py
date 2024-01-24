from django.contrib import admin
from .models import Jobs, JobsUser, Employer, EmployerEntity, JobCategory
# Register your models here.
admin.site.register(Jobs)
admin.site.register(JobsUser)
admin.site.register(Employer)
admin.site.register(EmployerEntity)
admin.site.register(JobCategory)


