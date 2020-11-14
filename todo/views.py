from django.http import HttpResponse
from django.shortcuts import render

import todo
from todo.models import Todo


# classで書き換えたい
def index(request):
    todo = Todo.objects.all()
    context = {'todo': todo}
    return render(request, 'todo/index.html', context)
