from django.urls import path 
from .views import  UserCreate

urlpatterns = [
    path("users/register/",UserCreate.as_view(), name ="usercreate"),
    # path("users/list/",RegisteredUsers.as_view(),name="get_all_users")
    path("verify/".UserVerify.as_view(),name="verify_the_user")
]