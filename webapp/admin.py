from django.contrib import admin
from webapp.models.task import Task
from webapp.models.status import Status
from webapp.models.type import Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'created_at')
    list_filter = ('id', 'title')
    search_fields = ('title', 'description', 'type', 'created_at')
    fields = ('title', 'description', 'status', 'type')

admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'id')

admin.site.register(Type, TypeAdmin)
