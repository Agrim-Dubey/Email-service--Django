from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User


# Create your views here.

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response ({
                "id":user.user_id,
                "name":user.student_name,
                "email":user.student_mail
                },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

