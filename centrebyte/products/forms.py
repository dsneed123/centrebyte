from django import forms
from .models import Item
from PIL import Image  # Make sure you have the Pillow library installed

class RegisterItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'descriptions', 'price', 'image', 'available_count']  # Exclude 'user' from fields

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            img = Image.open(image)
            width, height = img.size
            if width != height:
                raise forms.ValidationError("Image must have a square aspect ratio (width = height).")
        return image



class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'descriptions', 'image', 'available_count']
