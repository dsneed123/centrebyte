from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
#model for item. Items are the object of what is being sold on the website.

class Item(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the item")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the item")
    descriptions = models.TextField(max_length=250, help_text="Description of the item", default="No description.")
    image = models.ImageField(upload_to='product_images/', help_text="Image of the item", default="../static/404.png")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation time when an item is created
    purchase_count = models.PositiveIntegerField(default=0, help_text="Number of purchases")  # To track the number of purchases
    available_count = models.PositiveIntegerField(default=0, help_text="Number of items available")  # To track the availability count

    def __str__(self):
        return self.name