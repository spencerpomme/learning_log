"""
learning_logs url pattern
"""

from django.urls import path
from . import views

app_name = 'learning_logs' # this is how to set namespace in Django 2.0

urlpatterns = [
    # home
    path('', views.index, name='index'),
    # all topic pages
    path('topics/', views.topics, name='topics'),
]
