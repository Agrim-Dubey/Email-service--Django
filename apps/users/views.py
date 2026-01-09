from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User
# import smtplib
# from email.message import EmailMessage
from .tasks import send_verification_email


# Create your views here.

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            send_verification_email.delay(
                user.student_mail,
                user.verification_token
            )

            return Response({
                "id": user.id,
                "email": user.student_mail,
                "message": "Verification email sent"
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserVerify(APIView):
    def get(self, request):
        token = request.query_params.get("token")

        if not token:
            return Response({"error": "Token missing"}, status=400)

        try:
            user = User.objects.get(verification_token=token)
        except User.DoesNotExist:
            return Response({"error": "Invalid token"}, status=400)

        if user.is_verified:
            return Response({"message": "Already verified"}, status=200)

        user.is_verified = True
        user.save()

        return Response({"message": "Account verified"}, status=200)