from django.db import models
from sellers.models import Seller  # Import the Seller model from your separate app

class Item(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the item")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the item")
    descriptions = models.TextField(max_length=250, help_text="Description of the item", default="No description.")
    def get_default_seller():
        return Seller.objects.get(id=1)

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, help_text="The seller of the item", default=get_default_seller)
    image = models.ImageField(upload_to='product_images/', help_text="Image of the item", default="../media/404.png")
    # Add more fields as needed, e.g., category, brand, etc.

    def __str__(self):
        return self.name
