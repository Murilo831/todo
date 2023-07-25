
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
    
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)

