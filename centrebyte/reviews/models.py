from django.db import models
from django.contrib import auth
from products.models import Item
#creating object for review
class Review(models.Model):
    content = models.TextField(help_text="review text")
    rating = models.IntegerField(help_text="the rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="date and time of review")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    item = models.OneToOneField('Item', help_text="the item being sold", on_delete=models.CASCADE)



#creating object for seller
class Seller(models.Model):
    first_name = models.CharField(max_length=50,help_text="sellers first name")
    last_name = models.CharField(max_length=50,help_text="sellers last name")
    seller_email = models.EmailField(help_text="sellers email address")
  


