from django.urls import path
from . import views

urlpatterns = [
    # 1. 날씨 API 테스트 - 서울의 예보 데이터 확인하기
    path("", views.index),
    # 2. 예보 데이터 중 원하는 데이터만 DB에 저장
    path("save-deposit-data/", views.save_deposit_data),
    path("signup_deposit/<int:option_pk>", views.signup_deposit),
    path("deposit_product_list/", views.deposit_product_list),
    # path("deposit_product_detail/<int:deposit_pk>", views.deposit_product_detail),
    # # 3. 저장된 데이터 전체 조회
    # path("save-exchange-data/", views.save_exchange_data)
    # path("list-data/", views.list_data),
    # # 4. 특정 조건 데이터 확인: 섭씨 30도가 넘는 시간대 조회
    # path("hot-weathers/", views.hot_weathers)
]

