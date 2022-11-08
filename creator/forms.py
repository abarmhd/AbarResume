from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from . import models
from django.contrib.auth.models import User
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = ['picture','resume_file','address','age','sex','linkedin_url']

    

class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = models.ResumeEducation
        fields = ['education','title','start_year','end_year']
        


class ResumeSkillForm(forms.ModelForm):
    class Meta:
        model = models.ResumeSkill
        fields = ['skill','level']
        
        

class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = models.ResumeExperience
        fields = ['Company','start_date','end_date','working_now']
        widgets = {
            'start_date':DatePicker(),
            'end_date':DatePicker()
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )