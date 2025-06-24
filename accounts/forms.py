from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label="ユーザー名")

    def save(self, request):
        user = super().save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user
