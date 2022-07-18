import email
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120,null=True)
    email = models.EmailField(unique=True,null=True)
    adress = models.TextField(null=True)
    phonenumber = models.CharField(max_length=10, unique=True,null=True)
    branch = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


