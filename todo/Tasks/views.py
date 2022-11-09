from django.shortcuts import render, redirect


# Create your views here.
from .models import *
from .forms import *

def index(request):  
    tasks = Tasks.objects.all()
    
    
    my_form = TaskForm()
    
    if request.method =='POST':
        my_form = TaskForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        return redirect('/')
    contex = {'tasks' : tasks , 'my_form' : my_form}
    return render(request, "tasks/list.html", contex)


def updateTask(request, pk):
    tasks = Tasks.objects.get(id=pk)
    
    my_form = TaskForm(instance=tasks)
    
    if request.method == 'POST':
        my_form = TaskForm(request.POST, instance=tasks)
        if my_form.is_valid():
            my_form.save()
        return redirect('/')
    
    contex = {'my_form' : my_form}
    return render(request, 'update_task.html', contex)

def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item' : item}
    return render(request, 'tasks/delete.html', context)