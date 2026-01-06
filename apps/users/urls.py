from django.urls import path 
from .views import  UserCreate

urlpatterns = [
    path("users/register/",UserCreate.as_view(), name ="usercreate")
    
]