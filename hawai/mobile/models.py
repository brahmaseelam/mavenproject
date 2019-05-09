from django.db import models

# Create your models here.
class music(models.MODEL):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
