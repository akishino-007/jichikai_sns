from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # allauth のルートを統合
]