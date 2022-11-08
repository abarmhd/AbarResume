from django.db.models import Count
from django.shortcuts import render
from . import forms
from . import models as modelsc
from creator import models

def home(request):
    genders = models.Sex.objects.all()
    skills = models.Skill.objects.all()
    education = models.Education.objects.all()
    resume_list = models.Resume.objects.all()
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            resume_list = resume_list.filter(name__istartswith=name)

    if 'family' in request.GET:
        family = request.GET['family']
        if family:
            resume_list = resume_list.filter(family__istartswith=family)

    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            resume_list = resume_list.filter(age__lte=int(age))

    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            resume_list = resume_list.filter(sex=int(gender))

    if 'education' in request.GET:
        education = request.GET['education']
        if education:
            resume_list = resume_list.distinct().filter(resume_education__education=int(education))

    if 'skill' in request.GET:
        skill = request.GET['skill']
        if skill:
            resume_list = resume_list.distinct().filter(resume_skill__skill=int(skill))
    
    if 'company_count' in request.GET:
        company_count = request.GET['company_count']
        if company_count:
            resume_list = resume_list.distinct().annotate(exp_count=Count('resume_experience')).filter(exp_count__gte=int(company_count))

    if 'working_now' in request.GET:
        working_now = request.GET['working_now']
        working_now = check_working_now(working_now)
        resume_list = resume_list.distinct().filter(resume_experience__working_now=working_now)

    search_param = request.GET



    context= {
        'gender':genders,
        'skills':skills,
        'educations':education,
        'resume':resume_list,
        'par':search_param
    }
    return render(request,'finder/home.html',context)


def contact(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            contact_model = modelsc.Contact(
                name = form.cleaned_data['name'],
                family = form.cleaned_data['family'],
                email = form.cleaned_data['email'],
                message = form.cleaned_data['message']
            )
            contact_model.save()

    return render(request,'finder/contact.html',{'form':form})
def check_working_now(val):
    try:
        return {
            '1':True,
            '0':False,
            '-1':None
        }[val]
    except KeyError:
        return False
def profile(request,id):
    resume = models.Resume.objects.get(id = id)
    resume_skills = models.ResumeSkill.objects.filter(resume=resume)
    resume_educations = models.ResumeEducation.objects.filter(resume=resume)
    reumse_experience = models.ResumeExperience.objects.filter(resume=resume)
    context = {
        'resume':resume,
        'skills':resume_skills,
        'educations':resume_educations,
        'experience':reumse_experience
    }
    return render(request,'generator/home.html',context)