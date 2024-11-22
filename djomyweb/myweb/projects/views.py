
from django.shortcuts import render# type: ignore

def projects(request):
    return render(request,"projects.html")
