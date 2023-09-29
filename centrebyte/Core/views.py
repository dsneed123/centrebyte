from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from products.models import Item
# Create your views here.

def IndexView(request):
    items = Item.objects.all()  # Assuming you have a model called Item
    return render(request, "base.html", {'items': items})