from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin():
    list_display = ("email", "name", "is_active", "created_at")
    search_fields = ("email", "name")
    list_filter = ("is_active",)    