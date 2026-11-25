from django.db import models

class student(models.Model):
    name  = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True  ,blank=True)
    #image = models.ImageField()
    #file = models.FileField()
    #image = models.ImageField(upload_to='images/', null=True, blank=True)
    #file = models.FileField(upload_to='files/', null=True, blank=True)

class car(models.Model):
    car_name= models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

def __str__(self) -> str:
    return self.car_name



