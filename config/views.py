from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    form_class= UserCreationForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('login')