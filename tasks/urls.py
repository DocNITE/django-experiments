from django.urls import path

from .views import index, create_task, toggle_task, delete_task

urlpatterns = [
    path('', index),
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/toggle/', toggle_task, name='toggle_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
]