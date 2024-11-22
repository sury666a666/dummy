# about/views.py
from django.shortcuts import HttpResponse# type: ignore
from django.shortcuts import render# type: ignore
from django.template import loader # type: ignore

def index(request):
    return render(request,"index.html")
