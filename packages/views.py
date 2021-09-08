from django.shortcuts import render
from .forms import *
from .models import *

def add(request):
    choice = Multi(request.POST)
    package_form = addPackageForm(request.POST)
    form = addQuestionForm(request.POST)
    if form.is_valid() | package_form.is_valid():
        # print(form.cleaned_data)
        package_form.save()
        form.save()
        choice.save()

    context = {'package_form': package_form, 'form': form, 'choice': choice}
    return render(request, 'packages/add.html', context)

# Create your views here.
