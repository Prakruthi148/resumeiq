"""
frontend/views.py
==================
Responsibility: Render HTML page templates.
No business logic — just return pages.
"""

from django.shortcuts import render


def index(request):
    """Render the main single-page application."""
    return render(request, 'index.html')