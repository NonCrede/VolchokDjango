from django import forms
from .models import *


class addPackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"


class addQuestionForm(forms.ModelForm):
    class Meta:
        model = Ques
        fields = "__all__"