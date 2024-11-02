from django.contrib import admin
from .models import Student
from .models import Domain
from .models import Questions

admin.site.register(Student)
admin.site.register(Domain)
admin.site.register(Questions)
