from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['category', 'title', 'content', 'thumbnail1', 'thumbnail2', 'thumbnail3', 'file']