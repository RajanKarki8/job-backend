from django.db import models
from django.contrib.auth.models import User
class Job(models.Model):
    
    JOB_TYPE = [
    ('internship', 'Internship'),
    ('junior-developer', 'Junior-developer'),
    ('mid/sinior', 'Mid/Sinior')
    ]

    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=500)
    description = models.TextField() 
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPE)
    requirements = models.TextField(blank = True)
    experience = models.PositiveIntegerField(null = True, blank = True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-date_posted']
        
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    
    
class Company(models.Model):
    com_name = models.CharField(max_length = 200, null = True, blank = True)
    address = models.CharField(max_length= 300, blank=True, null=True)
    def __str__(self) -> str:
        return self.com_name
    
class Person(models.Model):
    
    Gender = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    firstname = models.CharField(max_length = 200, null = True, blank = True)
    lastname = models.CharField(max_length = 200,null = True, blank = True)
    address = models.CharField(max_length = 300, null = True, blank = True)
    resume = models.FileField(upload_to='files', default=True)
    
    gender = models.CharField(max_length = 200, choices = Gender)
    apply_to = models.ForeignKey(Job, on_delete = models.CASCADE)
    
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'