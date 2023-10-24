from django.db import models
from products.models import Item
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)