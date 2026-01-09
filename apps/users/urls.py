
from django.urls import path
from .views import UserCreate, UserVerify

urlpatterns = [
    path("users/register/", UserCreate.as_view()),
    path("verify/", UserVerify.as_view()),
]
