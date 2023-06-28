from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
