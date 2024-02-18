from django.shortcuts import render, redirect
from django.contrib import messages
from user_app import forms


def register(request):
    if request.method == "POST":
        register_form = forms.CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New user added!")
            return redirect('todolist')
    else:
        register_form = forms.CustomUserCreationForm()
    return render(request, 'register_template.html', {
        'register_form': register_form
    })
