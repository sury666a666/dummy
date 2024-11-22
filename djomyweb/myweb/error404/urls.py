from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('error404/', views.error404, name='error404'),
]

