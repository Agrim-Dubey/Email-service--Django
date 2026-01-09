from django.db import models

# Create your models here.


class User(models.Model):
    student_name=models.CharField(unique=False,null=False,max_length=30,default = "noname")
    student_number=models.IntegerField(unique=True,null=False)
    student_mail = models.EmailField(unique=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    verification_string = models.CharField(null=False,unique= True,max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
            return self.student_mail
        
        
        