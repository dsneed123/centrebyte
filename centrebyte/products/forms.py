from django import forms
from .models import Item
class RegisterItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'descriptions', 'price', 'image']  # Exclude 'user' from fields

    def __init__(self, *args, **kwargs):
        super(RegisterItemForm, self).__init__(*args, **kwargs)