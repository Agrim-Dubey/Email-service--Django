# serializers.py
from rest_framework import serializers
from .models import User
import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("student_name","student_number","student_mail")

    def create(self, validated_data):
        validated_data["verification_token"] = uuid.uuid4().hex
        return super().create(validated_data)
