from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import requests
import datetime
from .serializers import (
    DepositOptionsSerializer,
    DepositProductSerializer,
    SubscribedProductSerializer,
    DepositProductWithOptionsSerializer,
)
from .models import DepositOptions, DepositProduct, SubscribedProduct
from django.http import JsonResponse
from rest_framework import status
from accounts.models import User
from django.contrib.auth.decorators import login_required
import json

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def deposit_product_list(request):
    deposit_products = DepositProduct.objects.all()
    serializer = DepositProductWithOptionsSerializer(deposit_products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def index(request):
    api_key = "bfb3b88bf28e201b6a11b0ddadcdc8c9"
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    response = requests.get(url).json()
    return Response(response)

@api_view(["GET"])
def save_deposit_data(request):
    api_key = "bfb3b88bf28e201b6a11b0ddadcdc8c9"
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    records = DepositProduct.objects.all()
    records.delete()
    records2 = DepositOptions.objects.all()
    records2.delete()
    response = requests.get(url).json()
    baseList = response.get("result").get("baseList")
    optionList = response.get("result").get("optionList")

    for idx in range(len(baseList)):
        save_basedata = {
            "fin_co_no": baseList[idx]["fin_co_no"],
            "fin_prdt_cd": baseList[idx]["fin_prdt_cd"],
            "kor_co_nm": baseList[idx]["kor_co_nm"],
            "fin_prdt_nm": baseList[idx]["fin_prdt_nm"],
            "join_deny": baseList[idx]["join_deny"],
            "join_member": baseList[idx]["join_member"],
            "join_way": baseList[idx]["join_way"],
            "spcl_cnd": baseList[idx]["spcl_cnd"],
            "max_limit": baseList[idx]["max_limit"],
            "etc_note": baseList[idx]["etc_note"],
            "dcls_end_day": baseList[idx]["dcls_end_day"],
        }

        baseserializer = DepositProductSerializer(data=save_basedata)
        if baseserializer.is_valid():
            baseserializer.save()

    for idx in range(len(optionList)):
        save_optiondata = {
            "deposit_product": optionList[idx]["fin_prdt_cd"],
            "intr_rate_type": optionList[idx]["intr_rate_type"],
            "intr_rate_type_nm": optionList[idx]["intr_rate_type_nm"],
            "save_trm": optionList[idx]["save_trm"],
            "intr_rate": optionList[idx]["intr_rate"],
            "intr_rate2": optionList[idx]["intr_rate2"],
        }
        optionserializer = DepositOptionsSerializer(data=save_optiondata)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save()

    return Response({"message": "okay"})


# def save_saving_data(request):
#     api_key = 'cc3b5702bc7c6e37bba0e8596571d6d1'
#     url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
#     records = SavingOptions.objects.all()
#     records.delete()
#     records2 = SavingProduct.objects.all()
#     records2.delete()
#     response = requests.get(url).json()
#     baseList = response.get("result").get("baseList")
#     optionList = response.get("result").get("optionList")
#     total_count = response.get("result").get("total_count")

#     for idx in range(len(baseList)):
#         save_data = {
#             'fin_prdt_cd': baseList[idx]['fin_prdt_cd'],
#             'fin_co_no': baseList[idx]['fin_co_no'],
#             'kor_co_nm': baseList[idx]['kor_co_nm'],
#             'fin_prdt_nm': baseList[idx]['fin_prdt_nm'],
#             'join_deny': baseList[idx]['join_deny'],
#             'join_member': baseList[idx]['join_member'],
#             'join_way': baseList[idx]['join_way'],
#             'spcl_cnd': baseList[idx]['spcl_cnd'],
#             'max_limit': baseList[idx]['max_limit'],
#             'etc_note': baseList[idx]['etc_note'],
#             'dcls_end_day': baseList[idx]['dcls_end_day'],
#             'mtrt_int': baseList[idx]['mtrt_int'],
#         }
#         Productserializer = SavingProductSerializer(data=save_data)
#         if Productserializer.is_valid():
#             Productserializer.save()
#     for idx in range(len(optionList)):
#         save_data2 = {
#             'deposit_foreign_Key': optionList[idx]['fin_prdt_cd'],
#             'intr_rate_type': optionList[idx]['intr_rate_type'],
#             'intr_rate_type_nm': optionList[idx]['intr_rate_type_nm'],
#             'rsrv_type': optionList[idx]['rsrv_type'],
#             'rsrv_type_nm': optionList[idx]['rsrv_type_nm'],
#             'save_trm': optionList[idx]['save_trm'],
#             'intr_rate': optionList[idx]['intr_rate'],
#             'intr_rate2': optionList[idx]['intr_rate2'],
#         }
#         Optionserializer = SavingOptionsSerializer(data=save_data2)
#         if Optionserializer.is_valid():
#             Optionserializer.save()


#     return JsonResponse({'message': 'okay'})


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["POST"])
@login_required
def signup_deposit(request, option_pk):
    data = json.loads(request.body.decode('utf-8'))
    user = request.user
    depositOption = DepositOptions.objects.get(id=option_pk)
    deposit_product_instance = depositOption.deposit_product
    if SubscribedProduct.objects.filter(fin_prdt_cd=deposit_product_instance.fin_prdt_cd, save_trm=depositOption.save_trm):
        return Response({'message': 'already'})
    if user.left_money_for_financial == 1:
        user.left_money_for_financial = user.money_for_financial
    if user.money_for_financial != 0 and user.left_money_for_financial - int(data['amount']) >= 0:
        user.used_money_for_financial += int(data['amount'])
        user.left_money_for_financial = user.money_for_financial - user.used_money_for_financial
        user.save()
    save_data = {
        "type": "S",
        "fin_prdt_cd": deposit_product_instance.fin_prdt_cd,
        "kor_co_nm": deposit_product_instance.kor_co_nm,
        "fin_prdt_nm": deposit_product_instance.fin_prdt_nm,
        "max_limit": deposit_product_instance.max_limit,
        "amount": int(data['amount']),
        "dcls_end_day": deposit_product_instance.dcls_end_day,
        "intr_rate_type": depositOption.intr_rate_type,
        "intr_rate_type_nm": depositOption.intr_rate_type_nm,
        "save_trm": depositOption.save_trm,
        "intr_rate": depositOption.intr_rate,
        "intr_rate2": depositOption.intr_rate2,
    }
    serializer = SubscribedProductSerializer(data=save_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
        return Response({"message": "okay"})


@api_view(["GET"])
def get_user_grade(request):
    userGrade = {}
    userSubscribed = SubscribedProduct.objects.all()

    for subscribed in userSubscribed:
        print(subscribed.user.money_for_financial)

    # userData = userSubscribed.user_set.all()
    # print(userData)
    print("========here========")
    return Response({"message": "okay"})
