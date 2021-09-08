from django.conf import settings
import json
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.views.generic import TemplateView


class Ques(models.Model):
    question_text = models.CharField("Вопрос:", max_length=200, null=True)
    Ques_id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')


class Package(models.Model):
    name = models.CharField("Название пака:", max_length=200, null=True)
    Pack_id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')


class PaQues(models.Model):
    Pack = models.ManyToManyField(Package)
    Quest = models.ManyToManyField(Ques)



# Create your models here.
