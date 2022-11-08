from django.contrib import admin
from . import models


class Contact_List_Admin(admin.ModelAdmin):
    search_fields = ('message','name')
    list_display = ('name','family','create_time','message')
    list_filter = ('create_time',)


admin.site.register(models.Contact,Contact_List_Admin)