from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(unique=True,primary_key=True)
    student_name=models.CharField(unique=True,nullable=False)
    student_number=models.IntegerField(unique=True,nullable=False)
    student_mail = models.EmailField(unique=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.student_mail
        
        
        