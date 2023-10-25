
from django.views import View
from products.models import Item
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterItemForm,ItemUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from django.contrib import messages

import os,random
# Create your views here.
from reviews.models import Review

from django.db.models import Avg

class ProductView(LoginRequiredMixin, View):
    template_name = 'product.html'
    login_url = '/login/'

    def get(self, request, id):
        item = get_object_or_404(Item, pk=id)

        # Query all reviews related to the item and calculate the average rating
        reviews = Review.objects.filter(item=item).aggregate(avg_rating=Avg('rating'))

        # Extract the average rating from the result (it might be None if there are no reviews)
        average_rating = reviews['avg_rating']

        btc_price = get_bitcoin_price("bitcoin")
        btc_price = btc_price.replace(',', '')
        final_price = (Decimal(item.price) / Decimal(btc_price))

        banner_folder = "./static/banners"
        
        images = [f for f in os.listdir(banner_folder) if f.endswith('.jpg')]
        image = random.choice(images)
        context = {
            'item': item,
            'btc_price': round(final_price, 8),
            'id': id,
            'reviews': reviews,
            'average_rating': average_rating,
            'image' : image,
        }

        return render(request, self.template_name, context)

@login_required
def register_item(request):
    if request.method == 'POST':
        form = RegisterItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the user field to the currently logged-in user
            form.instance.user = request.user
            form.save()
            return redirect('success_page')  # Redirect to a success page after item registration
    else:
        form = RegisterItemForm()

    return render(request, 'register-item.html', {'form': form})
def success_page(request):
    # Assuming you want to display the most recently registered item
    item = Item.objects.latest('id')  # You can customize this query as needed

    context = {'item': item}
    return render(request, 'success.html', context)
@login_required
def user_items_list(request):
    current_user = request.user
    user_items = Item.objects.filter(user=current_user)
    return render(request, 'user_items_list.html', {'user_items': user_items})


def get_bitcoin_price(coin):
    url = f'https://www.google.com/search?q={coin}+price'
    # make a request to the website
    response = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the current price (Assuming the price is the first result)
    try:
        price = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
        # Remove "United States Dollar" from the end of the price
        price = price.replace(' United States Dollar', '')
        return price
    except AttributeError:
        return "Price not found"

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Replace YourItemModel with your item model

    if request.method == 'POST':
        # Handle the form submission and update the item's information
        item.name = request.POST['edit-name']
        item.price = request.POST['edit-price']
        item.descriptions = request.POST['edit-description']
        
        # Handle the uploaded image if needed
        if 'edit-image' in request.FILES:
            item.image = request.FILES['edit-image']

        item.save()
        return redirect('user_items_list')  # Redirect to the view displaying the list of user items

    return render(request, 'user_items_list')

