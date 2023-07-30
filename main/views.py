from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import CustomUserCreationForm
from main.models import Task


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
    """User tasks"""
    tasks = Task.objects.filter(completed=False, username=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})


def task_done(request):
    taskdone = Task.objects.filter(completed=True, username=request.user)
    return render(request, 'tasks_done.html', {'taskdone': taskdone})


def task_detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_detail.html', {'task': task})
