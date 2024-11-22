from django.shortcuts import HttpResponse# type: ignore
from django.shortcuts import render# type: ignore
from django.template import loader # type: ignore # type: ignor
def blogs(request):
    return render(request,"blogs.html")
