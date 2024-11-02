from django.urls import URLPattern, path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", csrf_exempt(views.register), name='register'),
]
