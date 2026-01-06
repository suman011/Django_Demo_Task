from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    priority = models.IntegerField(default=3)  # 1=high, 5=low
    city = models.CharField(max_length=120, blank=True)  # used for API integration demo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
