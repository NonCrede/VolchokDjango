from django.conf import settings
import json
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.views.generic import TemplateView


class Questions(models.Model):
    question_text = models.TextField("Вопрос:", blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.question_text


class Package(models.Model):
    name = models.CharField("Название пака:", max_length=200, null=True)
    Quest = models.ManyToManyField(Questions)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.name




# Create your models here.
