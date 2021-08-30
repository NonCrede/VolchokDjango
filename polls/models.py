from django.conf import settings
import json
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.views.generic import TemplateView


class Question(models.Model):
    question_text = models.CharField("Вопрос:", max_length=200)
    question_number = models.PositiveIntegerField("Номер:")

    def __str__(self):
        return self.question_text
