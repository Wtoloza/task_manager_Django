from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.createTask, name='index'),
]