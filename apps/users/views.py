from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status
from .models import Student
# import smtplib
# from email.message import EmailMessage
from .tasks import send_verification_email
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class StudentCreate(APIView):
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            send_verification_email.delay(
                user.student_mail,
                user.student_name
            )
            return Response({
                "id": user.id,
                "email": user.student_mail,
                "message": "Email has been sent"
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
