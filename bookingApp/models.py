from django.db import models

# Create your models here.  














class categories(models.Model):
     categoryname=models.CharField(max_length=50,default="",null=False)


class courses(models.Model):
     coursesname=models.CharField(max_length=50,default="",null=False)
     description=models.CharField(max_length=50,default="",null=False)
     categoryID=models.IntegerField()
     ispuplish=models.BooleanField()

     

class booking(models.Model):
     Fristname=models.CharField(max_length=50 ,default="",null=False)
     lastname=models.CharField(max_length=50 ,default="",null=False)
     Email=models.EmailField(max_length=50,default="",null=False)
     phonenumber=models.IntegerField(null=False)
     age=models.IntegerField(null=False)
     city=models.CharField(max_length=50,default="",null=False)