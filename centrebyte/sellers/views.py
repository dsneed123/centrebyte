from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterItemForm
# Create your views here.
def register_item(request):
    if request.method == 'POST':
        form = RegisterItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after item registration
    else:
        form = RegisterItemForm()

    return render(request, '../templates/register-item.html', {'form': form})
def register_seller(request):
    return render(request, 'register-seller.html')