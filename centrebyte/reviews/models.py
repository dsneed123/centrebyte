from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Item

class Review(models.Model):
    content = models.TextField(help_text="Review text")
    rating = models.PositiveIntegerField(
        help_text="The rating the reviewer has given",
        validators=[
            MaxValueValidator(5, "Rating cannot be greater than 5"),
            MinValueValidator(1, "Rating cannot be less than 1")
        ]
    )
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date and time of review")
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reviews")
    item = models.ForeignKey(Item, help_text="The item being sold", on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.creator} for {self.item}"
