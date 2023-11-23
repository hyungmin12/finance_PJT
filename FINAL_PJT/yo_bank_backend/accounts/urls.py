from django.urls import path
from .views import CustomUserDetailsView, CustomUserDetailsUpdateView

urlpatterns = [
    path('user/', CustomUserDetailsView.as_view(), name='custom-user-details'),
    path('user_update/', CustomUserDetailsUpdateView.as_view(), name='user-update'),
]
