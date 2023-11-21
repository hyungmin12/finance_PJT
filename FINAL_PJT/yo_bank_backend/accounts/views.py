from django.shortcuts import render
from dj_rest_auth.views import UserDetailsView
from .serializers import CustomUserDetailsSerializer


# Create your views here.
class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer