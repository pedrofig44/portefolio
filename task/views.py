from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProjectTask
from .forms import ProjectTaskForm
from datetime import datetime
from django.utils import timezone

# Optional function-based view for quick status updates via AJAX
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


class TaskListView(LoginRequiredMixin, ListView):
    model = ProjectTask
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        selected_date = self.request.GET.get('selected_date')
        
        if selected_date:
            try:
                date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            except ValueError:
                date = timezone.now().date()
        else:
            date = timezone.now().date()
            
        return ProjectTask.objects.filter(date=date).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_date = self.request.GET.get('selected_date', timezone.now().date().strftime('%Y-%m-%d'))
        context['selected_date'] = selected_date
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = ProjectTask
    form_class = ProjectTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')  # Added namespace prefix 'task:'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectTask
    form_class = ProjectTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:task_list')  # Added namespace prefix 'task:'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectTask
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:task_list')  # Added namespace prefix 'task:'

@login_required
@require_POST
def update_task_status(request, pk):
    try:
        task = ProjectTask.objects.get(pk=pk)
        status = request.POST.get('status')
        if status in dict(ProjectTask.Status.choices):
            task.status = status
            task.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid status'}, status=400)
    except ProjectTask.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Task not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)