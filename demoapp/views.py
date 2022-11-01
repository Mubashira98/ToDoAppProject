from django.shortcuts import render, redirect

from demoapp.forms import TodoForm
from demoapp.models import todo


# Create your views here.

def mainpage(request):
    return render(request,'indexx.html')

def add_todo(request):
    form = TodoForm()
    # todos = todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewtitle')
    return render(request,'add_todo.html',{'form':form })

def viewtitle(request):
    data = todo.objects.all()
    return render(request,'view.html',{'data':data})






