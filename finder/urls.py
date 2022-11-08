from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='search_home'),
    path('contact/',views.contact,name='contact'),
    path('profiles/<int:id>/',views.profile,name='profile_detail')

]