from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User  # Django の標準 User をインポート

# すでに登録されている場合は再登録しない
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)


