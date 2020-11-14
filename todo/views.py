from django.http import HttpResponse
from django.shortcuts import redirect, render

import todo
from todo.models import Todo

from .forms import *
from .models import *


# classで書き換えたい
def index(request):
    todo = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        # if form.is_valid():
            # print('valid ok')
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
        return redirect('/')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)
