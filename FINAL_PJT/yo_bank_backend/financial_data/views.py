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
from django.shortcuts import get_object_or_404

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
    if SubscribedProduct.objects.filter(user_id=user.id, fin_prdt_cd=deposit_product_instance.fin_prdt_cd, save_trm=depositOption.save_trm):
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
def get_deposit_recommend(request):
    tmp = [[] for _ in range(100000)]
    subscribed_products = SubscribedProduct.objects.all()
    ch_money_for_financial = request.user.money_for_financial
    for subscribed_product in subscribed_products:
        user_id = subscribed_product.user_id
        fin_prdt_nm = subscribed_product.fin_prdt_nm
        fin_prdt_cd = subscribed_product.fin_prdt_cd
        deposit_product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
        save_trm = subscribed_product.save_trm
        intr_rate = subscribed_product.intr_rate
        intr_rate2 = subscribed_product.intr_rate2
        user = get_object_or_404(User, id=user_id)
        money_for_financial = user.money_for_financial
        tmp[user_id].append([
            user_id,
            money_for_financial,
            deposit_product.kor_co_nm,
            fin_prdt_nm,
            save_trm,
            intr_rate,
            intr_rate2,
            deposit_product.spcl_cnd,
            deposit_product.join_way,
            deposit_product.join_member,
            deposit_product.etc_note,
        ])
    a0to50=[]
    if 0<= ch_money_for_financial <= 500000:
        for tm in tmp:
            for t in tm:
                if t:
                    if 0 <=int(t[1])<= 500000:
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)
    

    if 500001<= ch_money_for_financial <= 1000000:
        for tm in tmp:
            for t in tm:
                if t:
                    if 500001 <=int(t[1])<= 1000000:
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)
    
    if 1000001<= ch_money_for_financial <= 1500000:
        for tm in tmp:
            for t in tm:
                if t:
                    if 1000001 <=int(t[1])<= 1500000:
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)
    
    if 1500001<= ch_money_for_financial <= 2000000:
        for tm in tmp:
            for t in tm:
                if t:
                    if 1500001 <=int(t[1])<= 2000000:
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)


    if 2000001<= ch_money_for_financial <= 3000000:
        for tm in tmp:
            for t in tm:
                if t:
                    if 2000001 <=int(t[1])<= 3000000:
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)
    
    if 3000001 <= ch_money_for_financial:
        for tm in tmp:
            for t in tm:
                if t:
                    if 2000001 <=int(t[1]):
                        a0to50.append(t)
        dic_0to50 = {}
        for a in a0to50:
            if f'{a[2]},{a[3]},{a[4]}' not in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] = 1
            elif f'{a[2]},{a[3]},{a[4]}' in dic_0to50:
                dic_0to50[f'{a[2]},{a[3]},{a[4]}'] += 1
        result_list = []
        rank = 1
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:3]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_option = DepositOptions.objects.get(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                result_dic = {
                    'kor_co_nm' : tops[0],
                    'fin_prdt_nm' : tops[1],
                    'save_trm' : tops[2],
                    'intr_rate' : final_option.intr_rate,
                    'intr_rate2' : final_option.intr_rate2,
                    'intr_rate_type_nm' : final_option.intr_rate_type_nm,
                    'join_member' : deposit_product.join_member,
                    'join_way' : deposit_product.join_way,
                    'spcl_cnd' : deposit_product.spcl_cnd,
                    'etc_note' : deposit_product.etc_note,
                    'rank' : rank
                }
                rank += 1
                result_list.append(result_dic)
        return Response(result_list)