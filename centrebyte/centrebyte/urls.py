"""
URL configuration for centrebyte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin, auth
from django.urls import path, include  # Import the 'include' function
from products.views import ProductView
from Core.views import IndexView, search_items, baseView
from products.views import register_item, success_page, user_items_list, update_item
from . import views
from checkout.views import crypto_payment,delete_wallet
from .views import logout_view
from cart.views import *
from django.conf import settings
from django.conf.urls.static import static
from reviews.views import create_review, review_success
from django.contrib.auth.views import LoginView
from .views import signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("",  baseView, name='base_view'),
    path("accounts/password_reset/done/",auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("accounts/reset/done/",auth.views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
    path('', IndexView, name='index'),
    path('product/<int:id>/', ProductView.as_view(), name='product_view'),
    path('accounts/profile/', views.profile_view, name='profile'),
    # Add the URL pattern for item registration
    path('register-item/', register_item, name='register_item'), 
    path('success-page/', success_page, name='success_page'), # Replace 'your_app' with your app's name
    path('logout/', logout_view, name='logout'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('delete_from_cart/<int:cart_id>/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    path('accounts/profile/user_items/', user_items_list, name='user_items_list'),
    path('payment/', crypto_payment, name='crypto_payment'),
    path('payment/delete_wallet/', delete_wallet, name='delete_wallet'),
    path('create_review/<int:id>/', create_review, name='create_review'),
    path('review_success/<int:item_id>/', review_success, name='review_success'),
    path('search/', search_items, name='search_items'),
    path('accounts/register/', signup, name='signup'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)