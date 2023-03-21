from django.urls import path

from webapp.views.projects import ProjectDetailView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView, AddUser
from webapp.views.tasks import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('task/add/', TaskCreateView.as_view(), name = 'task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name = 'task_detail'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name = 'task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('task/projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('task/projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('tasks/delete_project/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('tasks/projects/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),
    path('tasks/project/<int:pk>/add_user', AddUser.as_view(), name='project_add_user'),

]