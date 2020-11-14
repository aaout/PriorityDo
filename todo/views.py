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
