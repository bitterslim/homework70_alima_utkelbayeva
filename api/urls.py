from api.views import TaskDetailView, TaskUpdateView, TaskDeleteView, ProjectDeleteView, ProjectUpdateView, \
    ProjectDetailView
from django.urls import path
urlpatterns = [
    path("task/<int:pk>", TaskDetailView.as_view(), name='task'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name='task_update'),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name='task_delete'),
    path("project/<int:pk>", ProjectDetailView.as_view(), name='task'),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name='task_update'),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name='task_delete'),
]