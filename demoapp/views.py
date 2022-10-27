from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request,'indexx.html')

def secondpage(request):
    return render(request,'second.html')