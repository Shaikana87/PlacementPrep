from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Questions
from .models import Domain
from .models import Student

def main(request):
    if request.user.is_authenticated:
        que_list = Questions.objects.all()
        domains = Domain.objects.all()
        students = Student.objects.all()
        return render(request, 'main.html', 
                {'que_list': que_list, 'domains': domains, 'students': students})
        # return render(request, 'main.html') 
    # messages.info(request, 'Please login with your credentials to access this page!')
    return  redirect('login')
