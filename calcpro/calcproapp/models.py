from django.db import models
class Information(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=200)



# Create your models here.
