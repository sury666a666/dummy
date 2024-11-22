from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
]

