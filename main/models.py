from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=120)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
