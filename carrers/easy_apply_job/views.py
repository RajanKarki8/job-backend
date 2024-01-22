from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application
from .forms import JobApplyForm, RegisterForm, AddJobForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit = False)
            job.created_by = request.user
            job.save()
            return redirect('index')
    else:
        form = AddJobForm()
    context = {'form':form}
    return render(request, 'easy_apply_job/add_job.html', context) 

def UserRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.username = form_data.email
            form_data.save()
            messages.info(request, 'register is success')
            return redirect('index')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'easy_apply_job/register.html', context)         

def index(request):
    jobs = Job.objects.all()
    context = {
        'jobs':jobs
    }
    return render(request,'easy_apply_job/listing.html', context)

def job_details(request, pk):
    job = get_object_or_404(Job, id=pk)
    context = {
        'job':job
    }  
    return render(request, 'easy_apply_job/detail.html', context)

def apply(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    if request.method == 'POST':
        form = JobApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.apply_to_id = pk
            person = form.save(commit=False)
            person.job = job
            person.save()
            messages.success(request, f'{person} applied for {job}')
            return redirect('index')
        
    else:
        form = JobApplyForm()
    context = {
            'form':form,
            'job':job
        }

    return render(request, 'easy_apply_job/apply_job.html', context)

def appliedjob(request):
    appliedjob = Job.objects.filter(application__isnull = True)
    
    return render(request, 'easy_apply_job/applied.html', {'appliedjob':appliedjob})