from django.urls import path, include
from . import views
from accounts.views import CustomConfirmEmailView

app_name = 'accounts'

urlpatterns = [
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),  # allauth のルートを統合
    path('accounts/profile/', views.profile_view, name='profile'),

]