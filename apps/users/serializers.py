# serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Student
        fields = ['id','name','student_number','email','created_at']
    
    def validate_email(self,value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("Student with this email has already been registered")
        return value
    def validate_student_number(self,value):
        if Student.objects.filter(student_number =  value).exists():
            raise serializers.ValidationError("Student with this student number has already been registered")
        return value