from django.shortcuts import render
from .forms import *
from .models import *

def add(request):
    package_form = addPackageForm(request.POST)
    form = addQuestionForm(request.POST)

    context = {'package_form': package_form, 'form': form}
    return render(request, 'packages/add.html', context)

# Create your views here.
