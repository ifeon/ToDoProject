from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from main.models import Task


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'detail', 'completed', 'username']
