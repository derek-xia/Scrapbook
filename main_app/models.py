from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=200)
    
