"""
config/urls.py
==============
Root URL configuration.
Each app registers its own urls.py — this file just wires them together.
"""

from django.urls import path, include

urlpatterns = [
    # Frontend pages (index page, etc.)
    path('', include('frontend.urls')),

    # Analyzer API endpoints (/api/...)
    path('api/', include('analyzer.api.urls')),
]