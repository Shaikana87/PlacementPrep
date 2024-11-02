from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def video(request):
    if request.user.is_authenticated:
        return render(request, 'videocontent.html') 
    return  redirect('login')
    