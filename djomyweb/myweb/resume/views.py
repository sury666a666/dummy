from django.shortcuts import HttpResponse# type: ignore
from django.shortcuts import render# type: ignore
from django.template import loader # type: ignore # type: ignor
def resume(request):
    return render(request,"resume.html")
