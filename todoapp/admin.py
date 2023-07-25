from django.contrib import admin

from .models import Task

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'update_at')
    search_fields = ('task',)# barra de pesquisa

admin.site.register(Task, TasksAdmin)