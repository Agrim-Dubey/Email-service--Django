from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ("student_mail", "student_number","created_at")
    search_fields = ("student_mail", "student_number") 