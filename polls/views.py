import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from packages.models import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import base64
from io import BytesIO
import PIL
from PIL import Image
import os


def im_2_b64(image):
    if len(image) > 2:
        with open("media/" + image, mode="rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('latin1')

        return encoded_string



class SomeTemplateView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = json.dumps(
            [
                {
                    'question_id': obj.id,
                    'question_text': obj.question_text,
                    'photo': im_2_b64(str(obj.photo)),
                }
                for obj in Questions.objects.all()
            ]
        )

        return context
