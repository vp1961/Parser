from django.shortcuts import render
from .models import Task

def index(request):
    return render(request, 'index.html', 
    context={'task_list':Task.objects.filter(is_done=True)})
