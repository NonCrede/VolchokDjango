from django import forms
from .models import *


class addPackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'Quest']


class addQuestionForm(forms.ModelForm):
    class Meta:
        model = Ques
        fields = ['question_text', 'photo']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 20}),
        }


#class Multi(forms.ModelForm):
    #class Meta:
      #  model = PaQues
        #fields = "__all__"