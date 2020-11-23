from django.db import models

# Create your models here


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    motivation = models.CharField(max_length=500, default='')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
