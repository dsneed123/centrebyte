from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Item
from django.shortcuts import render, get_object_or_404

# Create your views here.
def productView(request, id):
    # Get the item by its ID or return a 404 error page if it doesn't exist
    item = get_object_or_404(Item, id=id)
    
    # Now, you can pass the 'item' to the template for rendering
    return render(request, 'product.html', {'item': item})