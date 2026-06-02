from django.contrib import admin
from jobseeker.models import *  # hamko impot karna hoga
# Register your models here.
admin.site.register(user)
admin.site.register(jobseeker)