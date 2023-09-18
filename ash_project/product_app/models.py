from django.db import models

# Create your models here.

class Product(models.Model):

    name=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    cat=models.IntegerField()
    is_available=models.BooleanField()