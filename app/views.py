from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import path

def hello(request):
    return render(request, 'index.html')