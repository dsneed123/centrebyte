from django import forms
from .models import Review  # Import your Review model

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']