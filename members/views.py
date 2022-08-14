from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegistrationForm
from django.urls import reverse_lazy

# Create your views here.
class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_message = "You have registered successfully. Login to continue using the website"
    success_url = reverse_lazy('login')

