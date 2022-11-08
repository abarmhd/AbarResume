from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from creator import models

@login_required
def home(request):
    try:
        resume = get_object_or_404(models.Resume, user=request.user)
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
    except:
        return render(request,'generator/home.html')
