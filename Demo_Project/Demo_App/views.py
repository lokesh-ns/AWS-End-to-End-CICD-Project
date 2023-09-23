from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet_func(request):
    return HttpResponse ('<h1 style="color:red";> Hey there, welcome to Django Demo Project </h1>')