from django.db import models

# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    course=models.CharField(max_length=20)
    join_date=models.DateField()
    phone=models.CharField(max_length=10)

class Employee(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.CharField()
    phone_no=models.CharField(max_length=10)
    dept_no=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    commision=models.FloatField()
    salary=models.FloatField()
    address=models.CharField(max_length=30)
    