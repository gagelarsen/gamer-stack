"""
The gamerstack URL Configurations.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('gamestats/', include('gamestats.urls')),
    path('admin/', admin.site.urls),
]
