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
from Core.views import IndexView
from sellers.views import register_item,register_seller


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('product/<int:id>/', ProductView.as_view(), name='product_view'),

    # Add the URL pattern for item registration
    path('register-item/', register_item, name='register_item'),  # Replace 'your_app' with your app's name
    path('register-seller/', register_seller, name='register-seller'),
    path("accounts/", include(("django.contrib.auth.urls", "auth"),namespace="accounts" )),
    path("accounts/password_reset/done/", auth.views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("accounts/reset/done/", auth.views.PasswordResetCompleteView.as_view(), name="Passeord_reset_complete"),
]
