# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     nickname = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     money = models.IntegerField(blank=True, null=True)
#     salary = models.IntegerField(blank=True, null=True)
#     # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
#     financial_products = models.TextField(blank=True, null=True)
    
#     # superuser fields
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)


import random
import requests


# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = 'cc3b5702bc7c6e37bba0e8596571d6d1'

financial_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록
optionList = response.get('result').get('optionList') # 상품 옵션 목록
for product in baseList:
    for option in optionList:
        if product['fin_prdt_cd'] == option['fin_prdt_cd']:
            item = 'D,' + product['kor_co_nm']+','+product['fin_prdt_nm'] + ',' + option['save_trm'] +','+ product['fin_prdt_cd'] + ',' + option['intr_rate_type_nm'] + ',' + option['intr_rate_type'] +  ',' + str(option['intr_rate']) + ',' + str(option['intr_rate2'])
            financial_products.append(item)


p_base_tmp = [[] for _ in range(len(baseList))]
p_optionList_tmp = [[] for _ in range(len(optionList))]

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록
optionList = response.get('result').get('optionList') # 상품 옵션 목록
for product in baseList:
    for option in optionList:
        if product['fin_prdt_cd'] == option['fin_prdt_cd']:
            # item = 'S_'+ product['kor_co_nm']+'_'+option['save_trm']+'_' + product['fin_prdt_cd'] + '_' + option['intr_rate_type_nm'] + '_' + option['intr_rate_type'] +  '_' + str(option['intr_rate']) + '_' + str(option['intr_rate2'])
            item = 'S,' + product['kor_co_nm']+','+product['fin_prdt_nm'] + ',' + option['save_trm'] +','+ product['fin_prdt_cd'] + ',' + option['intr_rate_type_nm'] + ',' + option['intr_rate_type'] +  ',' + str(option['intr_rate']) + ',' + str(option['intr_rate2'])
            financial_products.append(item)
s_base_tmp = [[] for _ in range(len(baseList))]
s_optionList_tmp = [[] for _ in range(len(optionList))]
# print(financial_products)
#'D_WON플러스예금_6WR0001B_단리_S_4.02_4.02'


dict_keys = ['type', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 'max_limit', 'amount', 'dcls_end_day', 'rsrv_type', 'rsrv_type_nm',
            'intr_rate_type', 'intr_rate_type_nm', 'save_trm', 'intr_rate', 'intr_rate2', 'user_id']




import json
from collections import OrderedDict

file = OrderedDict()
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = './yo_bank_backend/financial_data/fixtures/subscribed_data.json'
len_s = len(financial_products)-1
N = 500
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    # print(type,kor_co_nm,fin_prdt_nm,save_trm,fin_prdt_cd,intr_rate_type_nm,intr_rate_type,intr_rate,intr_rate2)
    
    for i in range(N):
    # #         # 랜덤한 데이터를 삽입
        type,kor_co_nm,fin_prdt_nm,save_trm,fin_prdt_cd,intr_rate_type_nm,intr_rate_type,intr_rate,intr_rate2 = financial_products[random.randint(0, len_s)].split(',')
        # print()
        # print(type,kor_co_nm,fin_prdt_nm,save_trm,fin_prdt_cd,intr_rate_type_nm,intr_rate_type,intr_rate,intr_rate2)
        file["model"] = "financial_data.subscribedproduct"
        file["pk"] = i+1
        file["fields"] = {
            'type' : type,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'save_trm' : save_trm,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate_type' : intr_rate_type,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'max_limit' : 0,
            'amount' : random.randrange(10000, 300000, 10000),
            'dcls_end_day' : 0,
            'rsrv_type' : 0,
            'rsrv_type_nm' : 0,
            'user_id' : random.randint(1, 9999)
        }
        
        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')