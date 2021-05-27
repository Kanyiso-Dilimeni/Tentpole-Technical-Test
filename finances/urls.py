from django.urls import path

from . import views

app_name = 'finances'

"""
    Receives input from workflow_manager/urls.py and opens views.index
"""
urlpatterns = [
    path('', views.index, name='index'),
]
