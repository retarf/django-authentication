from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import UserForm

# Create your views here.

def index(request):
    context = {'content': 'Success'}
    return render(request, 'core/index.html', context)

def create(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()
            return redirect('index')
    else:
        form = UserForm()
    context = {'form': form}

    return render(request, 'core/create.html', context)

def list(request):
    users = User.objects.all()

    return render(request, 'core/list.html', {'users': users})

def change(request, pk):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.save()
            return redirect('index')
    else:
        user = User.objects.get(pk=pk)
        form = UserForm(initial={'username': user.username})
    context = {'form': form, 'pk': pk}

    return render(request, 'core/change.html', context)
