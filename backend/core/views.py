from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import UserForm, LoginForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username = username,
                password = password,
            )
            if user is not None:
                return redirect('core:index', user.pk)
        return redirect('core:login')
    else:
        form = LoginForm(request.POST)

    content = {'form': form}

    return render(request, 'core/login.html', content)

def index(request, pk):
    user = User.objects.get(pk=pk)
    content = {
        'pk': pk,
        'username': user.username
    }
    return render(request, 'core/index.html', content)

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
            return redirect('index', pk)
    else:
        user = User.objects.get(pk=pk)
        form = UserForm(initial={'username': user.username})
    context = {'form': form, 'pk': pk}

    return render(request, 'core/change.html', context)

def user_page(request, pk):
    content = {'content': 'Success', 'pk': pk}
    return render(request, 'core/user_page.html', content)
