from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from Dashboard.models import Student
# Create your views here.

def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            # user.password = form.cleaned_data['password']
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Saving data in Student Model
            student = Student(first_name = form.cleaned_data['first_name'],
                            last_name = form.cleaned_data['last_name'],
                            username = form.cleaned_data['username'],
                            email = form.cleaned_data['email'])
            student.save()

            return HttpResponseRedirect('/login', "user created")
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})
