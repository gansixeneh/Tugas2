from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    data_todolist = Task.objects.filter(user=request.user)

    context = {
        'name': username,
        'list_todolist': data_todolist,
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('todolist:show_todolist')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('todolist:login')
    response.delete_cookie('last_login')
    return response

def create_task_user(request):
    if request.method == 'POST':
        task_baru = Task()
        task_baru.user = request.user
        task_baru.date = str(datetime.date.today())
        task_baru.title = request.POST.get('title')
        task_baru.description = request.POST.get('description')
        task_baru.save()
        messages.success(request, 'Task baru telah berhasil ditambah!')
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'create-task.html', context)