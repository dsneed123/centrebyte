from django.db import models

from cart.models import Cart
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for your user profile.
    # For example, you can add a cart field here if it's related to the user's profile.
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

