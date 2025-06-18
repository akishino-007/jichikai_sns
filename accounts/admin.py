from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  

if not admin.site.is_registered(CustomUser):
    admin.site.register(CustomUser, UserAdmin)


