from django.db import models

# Create your models here.
from django.db import models

class Seller(models.Model):
    id = models.AutoField(primary_key=True)  # This line ensures 'id' is the primary key.
    name = models.CharField(max_length=50, help_text="Name of the seller")
    email = models.EmailField(help_text="Email address of the seller")
    # Add more fields for seller information as needed

    def __str__(self):
        return self.name