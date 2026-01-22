from django.urls import path
from .views import StudentCreate

urlpatterns = [
    path("users/register/", StudentCreate.as_view()),
]
