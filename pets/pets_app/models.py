from django.db import models

# Create your models here.
import uuid
from django.conf import settings

class Pet(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    breed = models.CharField(max_length=100)
    characteristics = models.JSONField()
    weight = models.FloatField()
    owner_document = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.species})"
   
    
