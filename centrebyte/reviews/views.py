from .models import Item
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

# Create your views here.


def create_review(request, id):
    item = get_object_or_404(Item, pk=id)  # Retrieve the item by its ID or handle a 404 if it doesn't exist

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.creator = request.user  # Associate the review with the current user
            review.item = item  # Set the item being reviewed
            review.save()
            return redirect(review_success, id)  # Redirect to the product detail page
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'item': item,  # Pass the item to the template for display
    }
    print('review created')
    return render(request, review_success, context)

def review_success(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }
    
    return render(request, 'review_success.html', context)