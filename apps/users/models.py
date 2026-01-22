from django.db import models

# Create your models here.


class Student(models.Model):
    student_name=models.CharField(unique=False,null=False,max_length=30,default = "noname")
    student_number=models.IntegerField(unique=True,null=False)
    student_mail = models.EmailField(unique=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.student_name} with the email : {self.student_mail}"
        
        
        