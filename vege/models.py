from django.db import models



class recepie(models.Model):
    recepie_name= models.CharField(max_length=100)
    recepie_descripiton = models.TextField()
    recepie_image = models.ImageField(upload_to="recepie")
    
