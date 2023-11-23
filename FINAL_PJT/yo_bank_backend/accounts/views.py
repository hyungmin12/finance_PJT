from django.shortcuts import render
from dj_rest_auth.views import UserDetailsView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from .serializers import CustomUserDetailsSerializer

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer
    

@permission_classes([IsAuthenticated])
class CustomUserDetailsUpdateView(APIView):
    def put(self, request):
        serializer = CustomUserDetailsSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    