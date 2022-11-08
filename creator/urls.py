from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='creator_home'),
    path('<int:resume_id>/',views.edit_resume,name='creator_edit_home'),
    path('skills/<int:resume_id>/',views.create_resume_skill,name='creator_skills'),
    path('experience/<int:resume_id>/',views.create_resume_experience,name='creator_experience'),
    path('educations/<int:resume_id>/',views.create_resume_education,name='creator_education'),
    
    #authentication
    path('registration/login/',auth_views.LoginView.as_view(),name='login'),
    path('registration/logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('registration/register/',views.register_view,name='register'),
    path('registration/profile/',views.profile,name='profile'),
    path('registration/edit-profile/',views.edit_profile,name='profile_edit'),
    path('registration/password/',views.change_pass,name='pass'),


]