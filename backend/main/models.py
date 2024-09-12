from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    author = models.ForeignKey(User,models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title