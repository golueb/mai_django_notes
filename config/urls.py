from django.contrib import admin
from django.urls import path, include
from notes.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('', include('notes.urls', namespace="notes")),
]
