from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, TaskList




class TaskListView(ListView):
    model = TaskList
    template_name = 'app/task_list.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return TaskList.objects.prefetch_related('tasks')


class TaskCreateView(CreateView):
    model = Task
    fields = ['task_list', 'title']
    template_name = 'app/task_form.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'app/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
