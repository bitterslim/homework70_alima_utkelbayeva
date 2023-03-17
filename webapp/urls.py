from django.urls import path

from webapp.views.tasks import TaskDetailView, TaskAddView, TaskUpdateView, TaskDeleteView
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('task/add/', TaskAddView.as_view(), name = 'task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name = 'task_detail'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name = 'task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete')
]