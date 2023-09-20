from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Seller
# Create your views here.

class IndexView(TemplateView):
    template_name = 'base.html'

def my_view(request, id):
    seller = Seller.objects.get(id=id)
    return HttpResponse(f"This seller's name is {seller.first_name} {seller.last_name}")