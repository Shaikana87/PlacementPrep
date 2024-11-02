from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("", views.main, name='main'),
]
