from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth import logout
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
    logout(request)