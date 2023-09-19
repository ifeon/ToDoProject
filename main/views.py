from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import CustomUserCreationForm, TaskCreationForm
from main.models import Task


def main(request):
    """Main page"""
    return render(request, 'base.html')


def user_login(request):
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
    task = get_object_or_404(Task,
                             id=id)
    return render(request, 'task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.username = request.user
            task.save()
            return redirect('main:profile')
    form = TaskCreationForm
    context = {
        'form': form,
    }
    return render(request, 'add_task.html', context)
