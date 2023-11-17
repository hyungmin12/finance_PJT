from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import datetime
from .serializers import DepositSerializer
from .models import Deposit
from django.http import JsonResponse

@api_view(['GET'])
def index(request):
    api_key = 'bfb3b88bf28e201b6a11b0ddadcdc8c9'
    url =  f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    return Response(response)

@api_view(['GET'])
def save_deposit_data(request):
    api_key = 'bfb3b88bf28e201b6a11b0ddadcdc8c9'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    baseList = response.get("result").get("baseList")
    optionList = response.get("result").get("optionList")
    total_count = response.get("result").get("total_count")

    for idx in range(total_count):
        save_data = {
            'dcls_month': baseList[idx]['dcls_month'],
            'kor_co_nm': baseList[idx]['kor_co_nm'],
            'fin_prdt_cd': baseList[idx]['fin_prdt_cd'],
            'fin_prdt_nm': baseList[idx]['fin_prdt_nm'],
            'join_way': baseList[idx]['join_way'],
            'mtrt_int': baseList[idx]['mtrt_int'],
            'spcl_cnd': baseList[idx]['spcl_cnd'],
            'join_member': baseList[idx]['join_member'],
            'etc_note': baseList[idx]['etc_note'],
            'dcls_strt_day': baseList[idx]['dcls_strt_day'],
            'fin_co_subm_day': baseList[idx]['fin_co_subm_day'],
            'intr_rate_type': optionList[idx]['intr_rate_type'],
            'intr_rate_type_nm': optionList[idx]['intr_rate_type_nm'],
            'save_trm': optionList[idx]['save_trm'],
            'intr_rate': optionList[idx]['intr_rate'],
            'intr_rate2': optionList[idx]['intr_rate2'],
        }
        serializer = DepositSerializer(data=save_data)
        if serializer.is_valid():
            serializer.save()

    return JsonResponse({'message': 'okay'})

@api_view(['GET'])
def save_exchange_data(request):
    api_key = 'cScsNMc43zgGq56PFZDLCLqWdRhiZizf'
    now = datetime.datetime.now()
    search_date = now.strftime("%Y%m%d")
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={search_date}&data=AP01'

    response = requests.get(url).json()
    return Response(response)