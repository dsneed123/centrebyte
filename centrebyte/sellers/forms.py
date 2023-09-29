from django import forms
# Create your models here.
from products.models import Item
class RegisterItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'descriptions', 'seller', 'image']