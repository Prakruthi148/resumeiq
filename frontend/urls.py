"""
frontend/urls.py
=================
URL routes for frontend HTML pages.
"""

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]