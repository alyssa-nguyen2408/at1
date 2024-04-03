from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    text = models.CharField(max_length=255)
    is_red = models.BooleanField(default=False)  # Indicates whether the question is marked as red to be used -> variable



class Sentence(models.Model):
    content = models.CharField(max_length=255)
    is_red = models.BooleanField(default=False)  # Add a BooleanField to track if the sentence is marked as red

    def __str__(self):
        return self.content
    


class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)