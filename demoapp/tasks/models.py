from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='todo')
    priority = models.IntegerField(default=3)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
