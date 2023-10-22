from django.shortcuts import render
from products.models import Item
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def cart_view(request):
    # Retrieve the items in the user's cart
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.price for cart in cart_items for item in cart.items.all())

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required
def add_to_cart(request, id):
    user = request.user
    item = get_object_or_404(Item, id=id)

    # Check if the user already has a cart
    cart, created = Cart.objects.get_or_create(user=user)

    # Add the item to the cart
    cart.items.add(item)
    print("Item added to your cart.")

    return redirect("cart_view")
@login_required
@require_POST
def delete_from_cart(request, cart_id, item_id):
    cart = get_object_or_404(Cart, id=cart_id, user=request.user)
    item = get_object_or_404(Item, id=item_id)
    cart.items.remove(item)
    return redirect("cart_view")

