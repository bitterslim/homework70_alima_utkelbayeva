from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import ProjectForm, TaskForm, AddUserForm
from webapp.models import Task
from webapp.models.project import Project


class ProjectDetailView(DetailView):
    template_name = 'project.html'
    model = Project

class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.create_project'
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'project_update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.update_project'



class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'project_delete.html'
    model = Project
    permission_required = 'webapp.delete_project'
    context_object_name = 'project'
    success_url = reverse_lazy('projects')

class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class AddUser(PermissionRequiredMixin, DetailView):
    model = Project
    template_name = 'add_user.html'
    form_class = AddUserForm
    permission_required = 'webapp.add_user'
    groups = ['admin', 'Product Manager', 'TeamLead']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save()
        user.project = project
        user.save()
        return redirect('project_detail', pk=project.pk)
