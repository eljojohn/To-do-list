from django.urls import path
from .views import TaskListView, TaskCreateView,TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('add/', TaskCreateView.as_view(), name='task-add'),
     path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
