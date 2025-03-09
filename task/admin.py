from django.contrib import admin
from .models import ProjectTask

@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'project_code', 'date', 'estimated_hours', 'status')
    list_filter = ('status', 'date', 'project')
    search_fields = ('project', 'project_code', 'activity')
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_per_page = 20