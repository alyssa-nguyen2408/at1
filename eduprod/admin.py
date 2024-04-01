from django import forms
from django.contrib import admin
from .models import Question
from .models import Sentence

# Register Question model with the default ModelAdmin
admin.site.register(Question)


admin.site.register(Sentence)