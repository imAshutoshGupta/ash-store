from django.db import models

# Create your models here.

class Product(models.Model):
    CAT=(
        (1,'Mobile'),
        (2,'Shoes'),
        (3,'Clothes')
    )       #used for making drop down choices and displaying the field
    AVAIL=((1,"Yes"),(0,"No"))

    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.FloatField()
    qty=models.IntegerField(verbose_name='Quantity')
    cat=models.IntegerField(verbose_name='Category', choices=CAT)
    is_available=models.BooleanField(verbose_name='Availability',choices=AVAIL)
    pdetails = models.CharField(verbose_name='Product Description',max_length=100)

    def __str__(self):          #string representation of the object
        #return str(self.id) #converting again to string as id is integer
        return self.name