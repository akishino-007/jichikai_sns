#from django.contrib.auth.models import User
#from django.urls import reverse_lazy
#from django.views.generic import CreateView

from .forms import SignupForm
from .models import CustomUser

# Create your views here.

#class SignupView(CreateView):
#    model = CustomUser
#    form_class = SignupForm
#    template_name = 'accounts/signup.html'
#    success_url = reverse_lazy('accounts:login')
