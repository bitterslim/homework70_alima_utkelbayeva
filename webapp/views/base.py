from django.views.generic import ListView
from webapp.models.task import Task


class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)
    queryset = Task.objects.all()

