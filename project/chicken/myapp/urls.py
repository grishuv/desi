# myapp/urls.py
from django.urls import path
from .views import index, login, registration

urlpatterns = [
    path('', index, name='index'),  # Set the empty path to the index view
    path('login/', login, name='login'),
      path('registration/', registration, name='registration'),  # Use a specific path for the login view
    # ... other URL patterns
]

