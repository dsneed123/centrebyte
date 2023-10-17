
from django.views import View
from products.models import Item
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
class ProductView(View):
    template_name = 'product.html'

    def get(self, request, id):
        # Retrieve the item with the specified ID or return a 404 page if it doesn't exist
        item = get_object_or_404(Item, pk=id)
        return render(request, self.template_name, {'item': item})

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