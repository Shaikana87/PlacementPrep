from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("", views.contests, name='contests'),
]
