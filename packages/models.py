from django.conf import settings
import json
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.views.generic import TemplateView


class Ques(models.Model):
    question_text = models.CharField("Вопрос:", max_length=200, null=True)
    question_number = models.PositiveIntegerField("Номер:", null=True)

    def __str__(self):
        return self.question_text


class Package(models.Model):
    name = models.CharField("Имя:", max_length=50, null=True)
    questions = models.ManyToManyField(Ques)

    def __str__(self):
        return self.name


# Create your models here.
