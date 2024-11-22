from django.shortcuts import render, redirect # type: ignore
from .models import Task

def index(request):
    tasks = Task.objects.all()
    
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('/')  # Redirect to the home page after adding a task

    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')  # Redirect to the home page after deleting a task
