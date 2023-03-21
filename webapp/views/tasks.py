
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm

from webapp.models.task import Task

class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Task


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'task_create.html'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    form_class = TaskForm
    template_name = "task_update.html"
    model = Task
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
