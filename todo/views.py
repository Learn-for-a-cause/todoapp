from django.shortcuts import render, redirect, get_object_or_404, reverse
from todo.models import Task
from todo.forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        return redirect("/")
    context = {"tasks": tasks, "form": form}
    return render(request, "index.html", context)

def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(reverse("list"))
    context = {"form" : form}
    return render(request, "update.html", context)

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.delete()
        return redirect(reverse("list"))
    context = {"task" : task}
    return render(request, "delete.html", context)
