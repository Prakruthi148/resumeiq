"""
analyzer/api/urls.py
=====================
URL routes for the analyzer API.
All routes here are prefixed with /api/ (set in config/urls.py).
"""

from django.urls import path
from .views import analyze_view

urlpatterns = [
    path('analyze/', analyze_view, name='api_analyze'),
]