from django.contrib import admin
from .models import Job, Person, Company, Application

admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Application)
admin.site.register(Company)