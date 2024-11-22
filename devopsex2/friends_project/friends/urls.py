from django.urls import path
from . import views

urlpatterns = [
    path('', views.friend_list, name='friend_list'),
    path('friend/new/', views.friend_create, name='friend_create'),
    path('friend/<int:pk>/edit/', views.friend_update, name='friend_update'),
    path('friend/<int:pk>/delete/', views.friend_delete, name='friend_delete'),
]
