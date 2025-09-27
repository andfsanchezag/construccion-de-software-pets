from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    owner = models.IntegerField()
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    characteristics = models.JSONField()
    weight = models.FloatField()
   
    
