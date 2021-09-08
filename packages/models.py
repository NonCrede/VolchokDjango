from django.conf import settings
import json
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.views.generic import TemplateView


class Ques(models.Model):
    question_text = models.CharField("Вопрос:", max_length=200, null=True)
    ques_id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')

    def __str__(self):
        return self.question_text


class Package(models.Model):
    name = models.CharField("Название пака:", max_length=200, null=True)
    Quest = models.ManyToManyField(Ques, null=True)
    pack_id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')

    def __str__(self):
        return self.name


class PaQues(models.Model):
    Pack = models.ManyToManyField(Package, null=True)
    Quest = models.ManyToManyField(Ques, null=True)



# Create your models here.
