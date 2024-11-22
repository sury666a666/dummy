# about/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]

