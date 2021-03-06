from django.http import HttpResponse
from django.shortcuts import redirect, render

import todo
from todo.models import Todo

from .forms import *
from .models import *


# classで書き換えたい
def index(request):
    todo = Todo.objects.all()
    # todo = Todo.objects.order_by('-motivation').all()
    form = TodoForm()
    # for i in range(len(todo)):
    #     todo[i].priority = todo[i].progress + todo[i].importance + todo[i].motivation
    #     todo[i].priority.save()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todo': todo, 'form':form}
    return render(request, 'todo/index.html', context)


def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            print('valid ok')
        return redirect('/')

    context = {'form':form}
    return render(request, 'todo/update.html', context)

def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        print(item.title)
        return redirect('/')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)

def sort_importance(request):
    todo = Todo.objects.order_by('-importance').all()
    context = {'todo':todo}
    return render(request, 'todo/sort_importance.html', context)


def sort_motivation(request):
    todo = Todo.objects.order_by('-motivation').all()
    context = {'todo':todo}
    return render(request, 'todo/sort_motivation.html', context)


def sort_progress(request):
    todo = Todo.objects.order_by('-progress').all()
    context = {'todo':todo}
    return render(request, 'todo/sort_progress.html', context)
