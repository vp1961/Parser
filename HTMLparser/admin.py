from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('url', ('minutes', 'seconds'))
    list_display = ('url', 'start_time', 'report', 'is_done', 'title', 'code', 'header')