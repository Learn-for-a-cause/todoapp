from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Task
        fields = '__all__'