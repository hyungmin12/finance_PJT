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
    SavingProductSerializer,
    SavingOptionsSerializer,
    SavingProductWithOptionsSerializer,
    SubscribedProductSerializer,
)
from .models import DepositOptions, DepositProduct, SubscribedProduct,SavingOptions,SavingProduct
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
def saving_product_list(request):
    saving_products = SavingProduct.objects.all()
    serializer = SavingProductWithOptionsSerializer(saving_products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def index(request):
    api_key = "bfb3b88bf28e201b6a11b0ddadcdc8c9"
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    response = requests.get(url).json()
    return Response(response)


@api_view(["GET"])
def save_saving_data(request):
    api_key = "bfb3b88bf28e201b6a11b0ddadcdc8c9"
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    records = SavingProduct.objects.all()
    records.delete()
    records2 = SavingOptions.objects.all()
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
    # print(save_basedata)

        baseserializer = SavingProductSerializer(data=save_basedata)
        if baseserializer.is_valid():
            baseserializer.save()

    for idx in range(len(optionList)):
        save_optiondata = {
            "saving_product": optionList[idx]["fin_prdt_cd"],
            "intr_rate_type": optionList[idx]["intr_rate_type"],
            "intr_rate_type_nm": optionList[idx]["intr_rate_type_nm"],
            "save_trm": optionList[idx]["save_trm"],
            "intr_rate": optionList[idx]["intr_rate"],
            "intr_rate2": optionList[idx]["intr_rate2"],
        }
        optionserializer = SavingOptionsSerializer(data=save_optiondata)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save()


    return Response({"message": "okay"})



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


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["POST"])
@login_required
def signup_deposit(request, option_pk):
    data = json.loads(request.body.decode('utf-8'))
    user = request.user
    flag = 0
    depositOption = DepositOptions.objects.get(id=option_pk)
    deposit_product_instance = depositOption.deposit_product

    if SubscribedProduct.objects.filter(user_id=user.id, fin_prdt_cd=deposit_product_instance.fin_prdt_cd, save_trm=depositOption.save_trm):
        return Response({'message': 'already'})
    if user.left_money_for_financial == 1:
        user.left_money_for_financial = user.money_for_financial
    if int(data['amount']) > user.left_money_for_financial:
        return Response({'message': 'dont have money'})
    if user.money_for_financial != 0 and user.left_money_for_financial - int(data['amount']) >= 0:
        user.used_money_for_financial += int(data['amount'])
        user.left_money_for_financial = user.money_for_financial - user.used_money_for_financial
        user.save()
        flag=1
        save_data = {
            "type": "D",
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

    if flag==0:
        save_data = {}    
    serializer = SubscribedProductSerializer(data=save_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
    return Response({"message": "okay"})

# @permission_classes([IsAuthenticatedOrReadOnly])
# @api_view(["POST"])
# @login_required
# def signup_deposit(request, option_pk):
#     data = json.loads(request.body.decode('utf-8'))
#     user = request.user
#     depositOption = DepositOptions.objects.get(id=option_pk)
#     deposit_product_instance = depositOption.deposit_product

#     save_data = None  # 초기값을 설정합니다.

#     if SubscribedProduct.objects.filter(user_id=user.id, fin_prdt_cd=deposit_product_instance.fin_prdt_cd, save_trm=depositOption.save_trm):
#         return Response({'message': 'already'})
#     if user.left_money_for_financial == 1:
#         user.left_money_for_financial = user.money_for_financial
#     if user.money_for_financial != 0 and user.left_money_for_financial - int(data['amount']) >= 0:
#         user.used_money_for_financial += int(data['amount'])
#         user.left_money_for_financial = user.money_for_financial - user.used_money_for_financial
#         user.save()
#         save_data = {
#             "type": "D",
#             "fin_prdt_cd": deposit_product_instance.fin_prdt_cd,
#             "kor_co_nm": deposit_product_instance.kor_co_nm,
#             "fin_prdt_nm": deposit_product_instance.fin_prdt_nm,
#             "max_limit": deposit_product_instance.max_limit,
#             "amount": int(data['amount']),
#             "dcls_end_day": deposit_product_instance.dcls_end_day,
#             "intr_rate_type": depositOption.intr_rate_type,
#             "intr_rate_type_nm": depositOption.intr_rate_type_nm,
#             "save_trm": depositOption.save_trm,
#             "intr_rate": depositOption.intr_rate,
#             "intr_rate2": depositOption.intr_rate2,
#         }

#     if save_data is not None:  # save_data가 정의되었는지 확인합니다.
#         serializer = SubscribedProductSerializer(data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=user)
#             return Response({"message": "okay"})
#     else:
#         return Response({'message': 'already'})


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(["POST"])
@login_required
def signup_saving(request, option_pk):
    data = json.loads(request.body.decode('utf-8'))
    user = request.user
    savingOption = SavingOptions.objects.get(id=option_pk)
    saving_product_instance = savingOption.saving_product
    print(saving_product_instance)
    if SubscribedProduct.objects.filter(user_id=user.id, fin_prdt_cd=saving_product_instance.fin_prdt_cd, save_trm=savingOption.save_trm):
        return Response({'message': 'already'})

    if user.left_money_for_financial == 1:
        user.left_money_for_financial = user.money_for_financial
    if user.money_for_financial != 0 and user.left_money_for_financial - int(data['amount']) >= 0:
        user.used_money_for_financial += int(data['amount'])
        user.left_money_for_financial = user.money_for_financial - user.used_money_for_financial
        user.save()
        save_data = {
            "type": "S",
            "fin_prdt_cd": saving_product_instance.fin_prdt_cd,
            "kor_co_nm": saving_product_instance.kor_co_nm,
            "fin_prdt_nm": saving_product_instance.fin_prdt_nm,
            "max_limit": saving_product_instance.max_limit,
            "amount": int(data['amount']),
            "dcls_end_day": saving_product_instance.dcls_end_day,
            "intr_rate_type": savingOption.intr_rate_type,
            "intr_rate_type_nm": savingOption.intr_rate_type_nm,
            "save_trm": savingOption.save_trm,
            "intr_rate": savingOption.intr_rate,
            "intr_rate2": savingOption.intr_rate2,
        }
    serializer = SubscribedProductSerializer(data=save_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user)
        return Response({"message": "okay"})


@api_view(["GET"])
def get_deposit_recommend(request):
    tmp = [[] for _ in range(10001)]
    subscribed_products = SubscribedProduct.objects.all()
    ch_money_for_financial = request.user.money_for_financial
    for subscribed_product in subscribed_products:
        if subscribed_product.type == 'D':
            user_id = subscribed_product.user_id
            fin_prdt_nm = subscribed_product.fin_prdt_nm
            fin_prdt_cd = subscribed_product.fin_prdt_cd
            deposit_product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
            save_trm = subscribed_product.save_trm
            intr_rate = subscribed_product.intr_rate
            intr_rate2 = subscribed_product.intr_rate2
            user = get_object_or_404(User, id=user_id)
            print(user,"======================")
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
            print(tmp[user_id])
            # print(tmp,"======================================")
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
        print("======================================")
        if len(dic_0to50) > 3:
            sorted_items = sorted(dic_0to50.items(), key=lambda x: x[1], reverse=True)
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                print("==========================")
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                print("=========gow==============")
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
        # print("============")
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = DepositProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = DepositOptions.objects.filter(deposit_product_id = fin_prdt_cd_for_deposit, save_trm = tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
    






@api_view(["GET"])
def get_saving_recommend(request):
    tmp = [[] for _ in range(100000)]
    subscribed_products = SubscribedProduct.objects.all()
    ch_money_for_financial = request.user.money_for_financial
    # print(ch_money_for_financial, "======================================")
    for subscribed_product in subscribed_products:
        if subscribed_product.type == 'S':
            user_id = subscribed_product.user_id
            fin_prdt_nm = subscribed_product.fin_prdt_nm
            fin_prdt_cd = subscribed_product.fin_prdt_cd
            deposit_product = SavingProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
            top_3_keys = [key for key, value in sorted_items[:10]]
            for top in top_3_keys:
                tops = top.split(',')
                deposit_product = SavingProduct.objects.get(kor_co_nm=tops[0], fin_prdt_nm=tops[1])
                fin_prdt_cd_for_deposit = deposit_product.fin_prdt_cd
                final_options = SavingOptions.objects.filter(saving_product_id=fin_prdt_cd_for_deposit, save_trm=tops[2])
                if final_options.exists():
                    # 여기서 결과를 처리
                    final_option = final_options.first()
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
    
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# @api_view(["GET"])
# def get_my_subscribed(request):
#     subs = SubscribedProduct.objects.filter(user=request.user)
#     serializer = SubscribedProductSerializer(subs, many=True)
#     deposits = []
#     for sub in subs:
#         deposit = DepositProduct.objects.get(fin_prdt_cd=sub.fin_prdt_cd)
#         deposits.append(DepositProductSerializer(deposit).data)
#     data = [serializer.data,deposits]
#     return Response(data)

from django.shortcuts import get_list_or_404

@api_view(["GET"])
def get_my_subscribed(request):
    subs = SubscribedProduct.objects.filter(user=request.user)

    # 리스트가 비어 있으면 404 에러 발생
    try:
        get_list_or_404(subs)
    except:
        return Response({'msg':'err'})

    serializer = SubscribedProductSerializer(subs, many=True)

    deposits = []
    for sub in subs:
        try:
            deposit = DepositProduct.objects.get(fin_prdt_cd=sub.fin_prdt_cd)
            deposits.append(DepositProductSerializer(deposit).data)
        except DepositProduct.DoesNotExist:
            pass
            # DepositProduct가 없는 경우에 대한 처리
            # deposits.append({"message": "DepositProduct does not exist"})
        try:
            savings = SavingProduct.objects.get(fin_prdt_cd=sub.fin_prdt_cd)
            deposits.append(SavingProductSerializer(savings).data)
        except SavingProduct.DoesNotExist:
            # DepositProduct가 없는 경우에 대한 처리
            pass
            # deposits.append({"message": "DepositProduct does not exist"})

    data = [serializer.data, deposits]
    return Response(data)



# @api_view(["POST"])
# def delete_product(request, subscribed_pk):
#     # 객체가 존재하지 않으면 404 에러 반환
#     sub = get_object_or_404(SubscribedProduct, pk=subscribed_pk)

#     # 여기에 삭제 권한 검증 코드 추가

#     # 객체 삭제
#     sub.delete()

#     return Response({'msg': 'SubscribedProduct deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
@api_view(["POST"])
def delete_product(request, subscribed_pk):
    # 객체가 존재하는지 확인
    subscribed_products = SubscribedProduct.objects.filter(pk=subscribed_pk)

    if subscribed_products.exists():
        # 여기에 삭제 권한 검증 코드 추가

        # 객체 삭제 (첫 번째 객체만 삭제)
        subscribed_products.first().delete()

        return Response({'msg': 'SubscribedProduct deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        # 객체가 존재하지 않으면 404 에러 반환
        # raise Http404("SubscribedProduct does not exist")
        return Response({'msg':'no object'})
