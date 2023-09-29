from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('register-item/', views.register_item, name='register_item'),
]