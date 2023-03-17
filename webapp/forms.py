from django.core.validators import MinLengthValidator, BaseValidator
from django import forms
from django.forms import widgets
from webapp.models import Task

class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value = 20):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value).s символов'
        super().__init__(limit_value=limit_value, message=message)


    def compare(self, value,limit_value):
        return value > limit_value



    def clean(self, value):
        return len(value)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'status','type', 'created_at','ended_at', 'description')
        labels = {
            'title': 'Task title',
            'description': 'Task description',
            'status': 'Task status',
            'type': 'Task type',
        }
        widgets = {
            'created_at': widgets.DateInput,
            'ended_at': widgets.DateInput
            }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')