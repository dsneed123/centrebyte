from django.db import models
from django.contrib import auth
#from reviews.models import Seller
 
class Item(models.Model):
    name = models.CharField(max_length=25, help_text="name of item")  
    price = models.IntegerField(help_text="price of item")
    seller = models.OneToOneField('Seller', on_delete=models.CASCADE, help_text="the seller of the item")