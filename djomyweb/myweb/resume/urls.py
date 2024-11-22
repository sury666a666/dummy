from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('resume/', views.resume, name='resume'),
]

