from django.db import models
from django.contrib.auth.models import User

#model for item. Items are the object of what is being sold on the website.
class Item(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the item") #name of item
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the item") #its price
    descriptions = models.TextField(max_length=250, help_text="Description of the item", default="No description.") #description
    image = models.ImageField(upload_to='product_images/', help_text="Image of the item", default="../static/404.png")
    # Add more fields as needed, e.g., category, brand, etc.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who owns the item
    def __str__(self):
        return self.name
