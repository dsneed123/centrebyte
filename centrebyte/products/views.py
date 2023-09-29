
from django.views import View
from products.models import Item
from django.shortcuts import render, get_object_or_404


class ProductView(View):
    template_name = 'product.html'

    def get(self, request, id):
        # Retrieve the item with the specified ID or return a 404 page if it doesn't exist
        item = get_object_or_404(Item, pk=id)
        return render(request, self.template_name, {'item': item})


