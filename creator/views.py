from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import forms
from django.forms import formset_factory
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse ,reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
@login_required
def home(request):
    try:
        if models.Resume.objects.get(user = request.user):
            id = models.Resume.objects.get(user = request.user)
            return HttpResponseRedirect(reverse('creator_edit_home',args=(id.id,)))
    except:
        form = forms.ResumeForm()
        if request.method == "POST":
            form = forms.ResumeForm(request.POST,request.FILES)
            if form.is_valid():
                resume = form.save(commit = False)
                resume.user = request.user
                resume.name = request.user.first_name
                resume.family = request.user.last_name
                resume.save()
                return HttpResponseRedirect(reverse('creator_edit_home',args=(resume.id,)))

        return render(request,'creator/home.html',{'form':form})

@login_required
def edit_resume(request,resume_id):
    try:
        if models.Resume.objects.get(user = request.user):
            id = models.Resume.objects.get(user = request.user)
            return HttpResponseRedirect(reverse('creator_edit_home',args=(id.id,)))
    except:
        resume = get_object_or_404(models.Resume,id=resume_id)
        if not resume.user == request.user:
            return render(request,'creator/home.html')
        form = forms.ResumeForm(instance=resume)
        return render(request,'creator/home.html',{'form':form})

@login_required
def create_resume_education(request,resume_id):
    try:
        if models.Resume.objects.get(user = request.user):
            id = models.Resume.objects.get(user = request.user)
            return HttpResponseRedirect(reverse('creator_edit_home',args=(id.id,)))
    except:
        resume = get_object_or_404(models.Resume,id=resume_id)
        educations = models.ResumeEducation.objects.filter(resume=resume)
        form = forms.ResumeEducationForm()
        if request.method == "POST":
            form = forms.ResumeEducationForm(request.POST)
            if form.is_valid():
                exprience = form.save(commit=False)
                exprience.resume = resume
                exprience.save()
                form = forms.ResumeEducationForm()
        return render(request,'creator/education.html',{'form':form,
                                                    'educations':educations,
                                                    'resume_id':resume.id
                                                    })
@login_required
def create_resume_skill(request,resume_id):
    try:
        if models.Resume.objects.get(user = request.user):
            id = models.Resume.objects.get(user = request.user)
            return HttpResponseRedirect(reverse('creator_edit_home',args=(id.id,)))
    except:
        resume_skill_formset = formset_factory(forms.ResumeSkillForm, extra=3)
        formset = resume_skill_formset()
        resume = get_object_or_404(models.Resume,id=resume_id)
        skills = models.ResumeSkill.objects.filter(resume=resume)
        if request.method == "POST":
            formset = resume_skill_formset(request.POST)
            if formset.is_valid():
                for form in formset:
                    exprience = form.save(commit=False)
                    exprience.resume = resume
                    exprience.save()
                    formset = resume_skill_formset()
        return render(request,'creator/skill.html',{'form':formset,'skill':skills,'resume_id':resume.id})

@login_required
def create_resume_experience(request,resume_id):
    try:
        if models.Resume.objects.get(user = request.user):
            id = models.Resume.objects.get(user = request.user)
            return HttpResponseRedirect(reverse('creator_edit_home',args=(id.id,)))
    except:
        form = forms.ResumeExperienceForm()
        resume = get_object_or_404(models.Resume,id=resume_id)
        experience = models.ResumeExperience.objects.filter(resume=resume)
        if request.method == "POST":
            form = forms.ResumeExperienceForm(request.POST)
            if form.is_valid():
                exprience = form.save(commit=False)
                exprience.resume = resume
                exprience.save()
                form = forms.ResumeEducationForm()
        return render(request,'creator/experience.html',{'form':form,'exper':experience,'resume_id':resume.id})


def register_view(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form =forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    return render(request,'registration/register.html',{'form':form})

@login_required
def profile(request):
    users = request.user
    return render(request,'registration/profile.html',{'user':users})

@login_required
def edit_profile(request):
    form = forms.EditProfileForm(instance=request.user)
    if request.method == "POST":
        form =forms.EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
    return render(request,'registration/edit_profile.html',{'form':form})

@login_required
def change_pass(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
    return render(request,'registration/change_pass.html',{'form':form})
