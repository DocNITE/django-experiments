from django.shortcuts import render, get_object_or_404 # should be used for empty/error/not verified or another answer
from django.http import JsonResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        task = Task.objects.create(text=text)
        return JsonResponse({'id': task.id, 'text': task.text, 'done': task.done})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return JsonResponse({'id': task.id, 'done': task.done})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return JsonResponse({'done': True})