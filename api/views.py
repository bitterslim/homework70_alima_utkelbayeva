from flask import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import TaskSerializer, ProjectSerializer
from webapp.models import Task, Project


class TaskDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TaskDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(pk, status=status.HTTP_200_OK)

class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

class ProjectUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProjectDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        project = Project.objects.get(id=pk)
        project.delete()
        return Response(pk, status=status.HTTP_200_OK)