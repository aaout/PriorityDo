from django import forms
from django.forms import ModelForm, fields

from .models import *


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'


class SortForm(forms.Form):
    SORT = {
        ('0', 'progress'),
        ('1', 'importance'),
        ('2', 'motivation'),
    }

    sort = forms.ChoiceField(label='sort', widget=forms.widgets.Select, choices=SORT, initial=0)
