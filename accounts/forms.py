from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

CustomUser = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user