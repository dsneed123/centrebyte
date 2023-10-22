from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from products.models import Item
from products.views import get_bitcoin_price
from decimal import Decimal
from reviews.models import Review
from django.db.models import Avg
from django.conf import settings
import os
import random


from django.db.models import F, ExpressionWrapper, DecimalField
from django.db.models import Avg
from datetime import timedelta



def baseView(request):
    # Get Bitcoin price
    btc_price = get_bitcoin_price("bitcoin")
    btc_price = btc_price.replace(',', '')  # Ensure the formatting is appropriate
    btc_price = Decimal(btc_price)  # Convert to a Decimal

    # Retrieve the average ratings for all items
    average_ratings = dict()
    reviews = Review.objects.values('item').annotate(avg_rating=Avg('rating'))
    for review in reviews:
        average_ratings[review['item']] = review['avg_rating'] if review['avg_rating'] is not None else 0

    # Sort the items based on the chosen criteria

    # Retrieve the four most popular items
    items_popular = Item.objects.order_by('-purchase_count')[:4]

    # Retrieve the four highest-rated items
    items_rated = Item.objects.annotate(
        avg_rating=Avg('review__rating')
    ).order_by('-avg_rating')[:4]

    # Retrieve the four newest items
    items_new = Item.objects.order_by('-created_at')[:4]

    # Calculate BTC price for every item category
    for item in items_popular:
        item.btc_price = round(Decimal(item.price) / btc_price, 8)
    for item in items_new:
        item.btc_price = round(Decimal(item.price) / btc_price, 8)
    for item in items_rated:
            item.btc_price = round(Decimal(item.price) / btc_price, 8)

    banner_folder = "./static/banners"
    
    images = [f for f in os.listdir(banner_folder) if f.endswith('.jpg')]
    image = random.choice(images)
    context = {
        'average_ratings': average_ratings,
        'items_popular': items_popular,
        'items_rated': items_rated,
        'items_new': items_new,
        'image': image, 
    }

    return render(request, "index.html", context)


def IndexView(request):
    sort_by = request.GET.get('sort_by', 'default')  # Get the sorting criteria from the query parameter

    items = Item.objects.all()
    btc_price = get_bitcoin_price("bitcoin")
    btc_price = btc_price.replace(',', '')  # Ensure the formatting is appropriate
    print(btc_price)
    btc_price = Decimal(btc_price)  # Convert to a Decimal

    final_prices = []  # List to store the final prices for all items
    average_ratings = {}  # Dictionary to store the average ratings for each item

    
    # Sort the items based on the chosen criteria
    if sort_by == 'price':
        items = sorted(items, key=lambda item: Decimal(item.price))
    elif sort_by == 'price_desc':
        items = sorted(items, key=lambda item: Decimal(item.price), reverse=True)
    elif sort_by == 'rating':
        items = sorted(items, key=lambda item: average_ratings.get(item.id, 0))
    elif sort_by == 'rating_desc':
        items = sorted(items, key=lambda item: average_ratings.get(item.id, 0), reverse=True)
    elif sort_by == 'created_at':
        items = sorted(items, key=lambda item: item.created_at)
    elif sort_by == 'oldest':
        items = sorted(items, key=lambda item: item.created_at)
    elif sort_by == 'newest':
        items = sorted(items, key=lambda item: item.created_at, reverse=True)
    elif sort_by == 'availability':
        items = sorted(items, key=lambda item: item.available_count)
    elif sort_by == 'most_available':
        items = sorted(items, key=lambda item: item.available_count, reverse=True)
    elif sort_by == 'least_available':
        items = sorted(items, key=lambda item: item.available_count)
    elif sort_by == 'most_purchased':
        items = sorted(items, key=lambda item: item.purchase_count, reverse=True)
    elif sort_by == 'least_purchased':
        items = sorted(items, key=lambda item: item.purchase_count)

    for item in items:
        final_price = Decimal(item.price) / btc_price
        final_prices.append(round(final_price, 8))
        reviews = Review.objects.filter(item=item).aggregate(avg_rating=Avg('rating'))
        average_ratings[item.id] = reviews['avg_rating'] if reviews['avg_rating'] is not None else 0  # Store average rating with item ID as the key, using 0 as the default

    final_items_with_prices = zip(items, final_prices)

    banner_folder = "./static/banners"
    
    images = [f for f in os.listdir(banner_folder) if f.endswith('.jpg')]
    image = random.choice(images)
    context = {
        'items_with_prices': final_items_with_prices,
        'average_ratings': average_ratings,
        'image': image,  # Pass the list of image file names to the template
    }
    
    return render(request, "base.html", context)



def search_items(request):
    search_query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'default')  # Get the sorting criteria from the query parameter

    items = Item.objects.filter(name__icontains=search_query)
    btc_price = get_bitcoin_price("bitcoin")
    btc_price = btc_price.replace(',', '')  # Ensure the formatting is appropriate
    print(btc_price)
    btc_price = Decimal(btc_price)  # Convert to a Decimal

    final_prices = []  # List to store the final prices for all items
    average_ratings = {}  # Dictionary to store the average ratings for each item

    
    # Sort the items based on the chosen criteria
    if sort_by == 'price':
        items = sorted(items, key=lambda item: Decimal(item.price))
    elif sort_by == 'price_desc':
        items = sorted(items, key=lambda item: Decimal(item.price), reverse=True)
    elif sort_by == 'rating':
        items = sorted(items, key=lambda item: average_ratings.get(item.id, 0))
    elif sort_by == 'rating_desc':
        items = sorted(items, key=lambda item: average_ratings.get(item.id, 0), reverse=True)
    elif sort_by == 'created_at':
        items = sorted(items, key=lambda item: item.created_at)
    elif sort_by == 'oldest':
        items = sorted(items, key=lambda item: item.created_at)
    elif sort_by == 'newest':
        items = sorted(items, key=lambda item: item.created_at, reverse=True)
    elif sort_by == 'availability':
        items = sorted(items, key=lambda item: item.available_count)
    elif sort_by == 'most_available':
        items = sorted(items, key=lambda item: item.available_count, reverse=True)
    elif sort_by == 'least_available':
        items = sorted(items, key=lambda item: item.available_count)
    elif sort_by == 'most_purchased':
        items = sorted(items, key=lambda item: item.purchase_count, reverse=True)
    elif sort_by == 'least_purchased':
        items = sorted(items, key=lambda item: item.purchase_count)

    for item in items:
        final_price = Decimal(item.price) / btc_price
        final_prices.append(round(final_price, 8))
        reviews = Review.objects.filter(item=item).aggregate(avg_rating=Avg('rating'))
        average_ratings[item.id] = reviews['avg_rating'] if reviews['avg_rating'] is not None else 0  # Store average rating with item ID as the key, using 0 as the default

    final_items_with_prices = zip(items, final_prices)

    banner_folder = "./static/banners"
    
    images = [f for f in os.listdir(banner_folder) if f.endswith('.jpg')]
    image = random.choice(images)
    context = {
        'items_with_prices': final_items_with_prices,
        'average_ratings': average_ratings,
        'image': image,  # Pass the list of image file names to the template
    }
    
    return render(request, "base.html", context)
