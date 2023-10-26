from django.db import models
from django.contrib.auth.models import User
from product_app.models import Product
# Create your models here.
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)