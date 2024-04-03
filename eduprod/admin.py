#importing
from django import forms
from django.contrib import admin
from .models import Question
from .models import Sentence
from .models import Essay


# Registering models with the default ModelAdmin
admin.site.register(Question)
admin.site.register(Sentence)
admin.site.register(Essay)