
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
]

