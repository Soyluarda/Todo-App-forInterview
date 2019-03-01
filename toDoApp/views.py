# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate,login
from .serializers import TodoSerializer
from .models import toDo
from .forms import toDoForm
from django.views.generic import View
from rest_framework import viewsets
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm



class TodoView(viewsets.ModelViewSet):
    queryset = toDo.objects.all()
    serializer_class = TodoSerializer




def index(request):
    todo_list = toDo.objects.order_by('id')
    form = toDoForm()
    context = {'todo_list':todo_list, 'form':form}
    return render(request,'todo/index.html',context)

@require_POST
def addToDo(request):
    form = toDoForm(request.POST)
    if form.is_valid():
        new_todo = toDo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeToDo(request,todo_id):
    todo = toDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def NotToDo(request,todo_id):
    todo = toDo.objects.get(pk=todo_id)
    todo.complete = False
    print (todo.complete)
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    toDo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    toDo.objects.all().delete()
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UserCreationForm()
        args = {'form':form}
        return render(request,'todo/registration_form.html',args)









































