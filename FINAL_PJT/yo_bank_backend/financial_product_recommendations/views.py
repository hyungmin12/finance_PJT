from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
# from .serializers import WeatherSerializers
# from .models import Weather

# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = 'bfb3b88bf28e201b6a11b0ddadcdc8c9'
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    return Response(response)