# AbarResume
**Django** `Resume Creator` WebApp<br>
### type to `cmd` :<br>
- create super user :<br>
>python manage.py createsuperuser<br>
- run in localhost :<br>
>python manage.py runserver 
<br>

## warnings:
this project dont need to apply migration or makemigrations so dont do that<br>
but if you need to migration or makemigrations go to `models.py` in `creator app` and delete `default=User.is_authenticated` in line 24<br>
after makemigrations or migrate then put code again<br>
## Required libraries
`django` , `pillow` , `django-tempus-dominus`<br><br>
for install libraries :
>pip install `your library name`

