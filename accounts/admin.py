from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  

#if not admin.site.is_registered(CustomUser):
#    admin.site.register(CustomUser, UserAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("追加情報", {"fields": ("bio", "birthyear", "kumi")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("追加情報", {"fields": ("bio", "birthyear", "kumi")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

