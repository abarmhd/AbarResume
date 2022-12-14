# Generated by Django 4.1 on 2022-10-17 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creator', '0002_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('picture', models.ImageField(default='media/pictures/no-img.jpg', upload_to='media/pictures/')),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='media/files/')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('sex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sex', to='creator.sex')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(default=5)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_skill', to='creator.resume')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='creator.skill')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('working_now', models.BooleanField(default=False)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_experience', to='creator.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_year', models.PositiveBigIntegerField(blank=True)),
                ('end_year', models.PositiveBigIntegerField(blank=True)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='creator.education')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_education', to='creator.resume')),
            ],
        ),
    ]
