from django.db import models
from django.forms import ModelForm
from django import forms

PRIORITIES = (
        ('adanger', 'Priority 1'),
        ('bwarning', 'Priority 2'),
        ('csuccess', 'Priority 3'),
        ('dprimary', 'Priority 4')
    )

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
                    max_length=30,
                    choices=PRIORITIES,
                    default=PRIORITIES[0][0]
                )
    complete = models.IntegerField(default=0)

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'date_of_creation']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's on your mind today?"}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your note ..", 'cols': 80, 'rows': 3}),
        }
