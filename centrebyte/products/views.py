from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from .models import Item

from django.shortcuts import render, get_object_or_404
from .models import Item  # Import your Item model

class ProductView(View):
    template_name = 'product.html'

    def get(self, request, id):
        # Retrieve the item with the specified ID or return a 404 page if it doesn't exist
        item = get_object_or_404(Item, pk=id)
        return render(request, self.template_name, {'item': item})
