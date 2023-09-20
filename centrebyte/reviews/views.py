from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Item
from django.shortcuts import render, get_object_or_404
# Create your views here.

class IndexView(TemplateView):
    template_name = 'base.html'


