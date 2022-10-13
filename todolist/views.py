from django.shortcuts import render
from todolist.models import Task
from todolist.forms import CreatNewTask
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
# Create your views here.

# variables for todolist.html
@login_required(login_url='/todolist/login')
def show_todolist(request):
    task_obeject = Task.objects.filter(user=request.user)
    user = request.user
    context = {
        'username_login': request.COOKIES['user_name'],
        'task_object': task_obeject,
        'user' : user,

    }
    return render(request, 'todolist.html', context)

# logic for register
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

# logic for login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('user_name', username)
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# logic for log out
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/todolist/login/")
def create_task(request):
    form = CreatNewTask(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()

        return redirect('todolist:show_todolist')
    context = {'form' : form}
    return render(request, 'create-task.html', context)

# logic update task
def update_task(request, id):
    task = Task.objects.get(pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

# logic delate task
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task_ajax(request):
    # form = CreatNewTask(request.POST)
    if request.method == 'POST' :
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user

        Task.objects.create(
            user = user,
            title = title,
            description = description,
        )

        #task = form.save(commit=False)
        #task.user = request.user
        #task.save()
    return JsonResponse({}, status=200)
   

# logic update task ajax
def update_task_ajax(request, id):
    if request.method == 'POST': 
        task = Task.objects.get(pk=id)
        task.is_finished = not task.is_finished
        task.save()
    return JsonResponse({}, status=200)


# logic delate task ajax
def delete_task_ajax(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.delete()
    return JsonResponse({}, status=200)
