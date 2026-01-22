# serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Student
        fields = ['id','student_name','student_number','student_mail','created_at']
    
    def validate_student_mail(self,value):
        if Student.objects.filter(student_mail=value).exists():
            raise serializers.ValidationError("Student with this email has already been registered")
        return value
    def validate_student_number(self,value):
        if Student.objects.filter(student_number =  value).exists():
            raise serializers.ValidationError("Student with this student number has already been registered")
        return value