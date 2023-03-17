from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm

from webapp.models.task import Task

class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Task


class TaskAddView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'task_create.html'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    template_name = "task_update.html"
    model = Task
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('webapp:index')
