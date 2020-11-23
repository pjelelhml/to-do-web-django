from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Adicione uma nova tarefa...'}))

    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Descreva a tarefa...'}
    ))

    motivation = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Qual a importância da tarefa?'}
    ))

    class Meta:
        model = Task
        fields = '__all__'
