from django.urls import path
from .views import register  # Ensure you're importing the correct view

urlpatterns = [
    path('register/', register, name='register'),  # Use 'register/' instead of an empty string
]
