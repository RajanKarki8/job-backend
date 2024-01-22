from django.forms import forms, ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'description', 'job_type', 'requirements']

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']

class JobApplyForm(ModelForm):
    
    class Meta:    
        model = Person
        fields = ['firstname', 'lastname', 'address', 'apply_to', 'resume']
        
    
    firstname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}),
    )

    lastname = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}),
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Enter address'}),
        required=False
    )

    # gender = forms.ChoiceField(
    #     choices=Person.Gender,
    #     widget=forms.RadioSelect,
    # )
    
    resume = forms.FileField(
        label = 'Resume', 
        widget=forms.ClearableFileInput(attrs={'placeholder': True}), 
        required=False
    )