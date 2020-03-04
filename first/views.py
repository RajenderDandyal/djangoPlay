from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'indexFirst.html', {'name': 'Rajender Dandyal'})


def home(request):
    return HttpResponse('Home Page')


def profile(request):
    return HttpResponse('Profile Page')

def add(request):
    val1 = float(request.GET['num1'])
    val2 = float(request.GET['num2'])
    res = val1 + val2
    
    return render(request, 'result.html', {'result': res})


def addPost(request):
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res = val1 + val2
    
    return render(request, 'result.html', {'result': res})  