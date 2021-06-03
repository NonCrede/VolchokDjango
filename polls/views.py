import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.views.generic import TemplateView

class SomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = json.dumps(
            [
                {
                    'id': obj.id,
                    'question_text': obj.question_text

                }
                for obj in Question.objects.all()
            ]
        )

        return context