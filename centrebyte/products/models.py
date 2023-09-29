from django.db import models
from sellers.models import Seller  # Import the Seller model from your separate app


#model for item. Items are the object of what is being sold on the website.
class Item(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the item") #name of item
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the item") #its price
    descriptions = models.TextField(max_length=250, help_text="Description of the item", default="No description.") #description
    def get_default_seller():
        return Seller.objects.get(id=1) # get the default seller, this will change to get_seller(id), where the od = the id of the sellers account.

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, help_text="The seller of the item", default=get_default_seller)  #set the foreign seller, right now it is default seller.
    image = models.ImageField(upload_to='product_images/', help_text="Image of the item", default="../static/404.png")
    # Add more fields as needed, e.g., category, brand, etc.

    def __str__(self):
        return self.name
