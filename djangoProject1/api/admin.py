from django.contrib import admin
from api.models import Student


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
