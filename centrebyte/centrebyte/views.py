from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, SignUpForm
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Core.views import IndexView
from cart.models import Cart
@login_required
def profile_view(request):
    user = request.user
    form = UserProfileForm(instance=user)  # Create an instance of the form
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the profile page or any other page as needed.
            return redirect('profile')
    
    return render(request, 'registration/profile.html', {'user': user, 'form': form})  # Include the form in the context
def logout_view(request):
    # Logout the user
    logout(request)
    # Redirect to the index page or any other page you want
    return redirect('index')  # 'index' should be the name of the URL pattern for your index page

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            Cart.objects.get_or_create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

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
        return redirect('user_item_list.html')  # Redirect to the view displaying the list of user items

    return render(request, 'products', {'item': item})