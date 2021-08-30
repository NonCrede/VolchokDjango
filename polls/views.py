import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class SomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = json.dumps(
            [
                {
                    'id': obj.id,
                    'question_text': obj.question_text,
                    'question_number': obj.question_number

                }
                for obj in Question.objects.all()
            ]
        )

        return context
