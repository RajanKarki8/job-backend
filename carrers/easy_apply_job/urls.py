from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('apply/<int:pk>/', views.apply, name = 'apply'),
    path('job-detail/<int:pk>/', views.job_details, name='job-detail'),
    path('register/', views.UserRegister, name = 'register'),
    path('add-job/', views.add_job, name = 'add-job'),
    path('applied', views.appliedjob, name = 'applied')
]
