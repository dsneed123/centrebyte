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
from products.views import register_item, success_page
from . import views
from .views import logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/",auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("accounts/reset/done/",auth.views.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
    path('', IndexView, name='index'),
    path('product/<int:id>/', ProductView.as_view(), name='product_view'),
    path('accounts/profile/', views.profile_view, name='profile'),
    # Add the URL pattern for item registration
    path('register-item/', register_item, name='register_item'), 
    path('success-page/', success_page, name='success_page'), # Replace 'your_app' with your app's name
    path('logout/', logout_view, name='logout'),
   
]
