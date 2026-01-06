from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'deadline']
        widgets = {'deadline' : forms.DateInput(attrs = {'type' : 'date'})}

class TaskfilterForm(forms.Form):
    status = [('', 'All') ,('in Progress', 'in Progress'), ('completed', 'Completed'), ('To-Do', 'To-do')]
    priority = [ ('', 'All') ,('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    
    status = forms.ChoiceField(required = False, choices = status)
    priority = forms.ChoiceField(required = False, choices = priority)