from django.urls import path 


urlpatterns = [
    path("users/register/",register_user.as_view())
    
]