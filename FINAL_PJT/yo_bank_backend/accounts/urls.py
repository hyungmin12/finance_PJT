from django.urls import path
from .views import CustomUserDetailsView  # Import your view

urlpatterns = [
    path('user/', CustomUserDetailsView.as_view(), name='custom-user-details'),
]
