from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import CustomUserCreationForm


def main(request):
    """Main page"""
    return render(request, 'base.html')


def login(request):
    return render(request, 'registration/login.html')


class RegView(CreateView):
    """Registration"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def profile(request):
    """User profile"""
    return render(request, 'profile.html')
