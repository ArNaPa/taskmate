from django.shortcuts import redirect
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required   # Restrict a view to login


@login_required             # This view required user to login
# Create your views here.
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            # 'commit=False' Delaying save option
            # '.manage' access to manage field
            # 'request.user' change value to current user
            form.save(commit=False).manage = request.user
            form.save()
        messages.success(request, "New message added!")
        return redirect('todolist')
    else:
        # all_task = Tasklist.objects.all()  # See All Task
        user_filter_task = Tasklist.objects.filter(manage=request.user)  # See All Task
        paginator = Paginator(user_filter_task, 5)  # See Filter User Task
        page = request.GET.get('pg')
        user_filter_task = paginator.get_page(page)
        user_filter_task.end_index()

        return render(request, 'welcome.html', {
            "all_objects": user_filter_task,
        })


def index(request):
    return render(request, 'index.html', {"str1": "HOME"})


@login_required
def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, "Not allowed")
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


@login_required
def alternate_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        if task.done:
            task.done = False
        else:
            task.done = True
    task.save()
    return redirect('todolist')


def contact(request):
    return render(request, 'contact.html', {"str1": "Welcome to contact app"})


def about(request):
    return render(request, 'about.html', {"str1": "Welcome to about app"})
