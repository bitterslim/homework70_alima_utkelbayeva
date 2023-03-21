from django.contrib.auth.models import User
from django.core.validators import BaseValidator
from django import forms
from webapp.models import Task, Status
from webapp.models.project import Project


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value = 20):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value).s символов'
        super().__init__(limit_value=limit_value, message=message)


    def compare(self, value,limit_value):
        return value > limit_value



    def clean(self, value):
        return len(value)

class TaskForm(forms.ModelForm):
    created_at = forms.CharField(required=True, label='Created at', widget= forms.SelectDateWidget)
    ended_at = forms.CharField(required=True, label='End at', widget=forms.SelectDateWidget)
    status = forms.ModelChoiceField(required=True,label='Status',queryset=Status.objects.all(), widget=forms.Select)
    project = forms.ModelChoiceField( required=False,label='Project',queryset=Project.objects.all(),widget=forms.Select)

    class Meta:
        model = Task
        fields = ('title', 'status','type', 'created_at','ended_at', 'description')
        labels = {
            'title': 'Task title',
            'description': 'Task description',
            'status': 'Task status',
            'type': 'Task type',
            'created_at': 'Created at'
        }


class ProjectForm(forms.ModelForm):
    start_date= forms.CharField(required=True, label='Started at', widget=forms.SelectDateWidget)
    finish_date= forms.CharField(required=True, label='Finish to', widget=forms.SelectDateWidget)
    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'finish_date')
        labels = {
            'title': 'Project title',
            'description': 'Project description',
            'start_date': 'Started at',
            'finish_date': 'Finish to'
        }
class AddUserForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Project
        fields = ('user', )
        labels = {
            'user': 'User'
        }