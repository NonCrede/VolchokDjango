from django.shortcuts import render
from .forms import *
from .models import *

def add(request):
    package_form = addPackageForm(request.POST)
    form = addQuestionForm(request.POST, request.FILES)
    if form.is_valid() and package_form.is_valid():
        # print(form.cleaned_data)
        form.save()
        package_form.save()
    else:
        package_form = addPackageForm()
        form = addQuestionForm()

    context = {'package_form': package_form, 'form': form}
    return render(request, 'packages/add.html', context)

# Create your views here.
