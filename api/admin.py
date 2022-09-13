from django.contrib import admin
from .models import Student, Sponsor, University
# Register your models here.


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('id', 'first_name','university','price')