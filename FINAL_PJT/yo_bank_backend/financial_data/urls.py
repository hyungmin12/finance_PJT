from django.urls import path
from . import views

urlpatterns = [
    # 1. 날씨 API 테스트 - 서울의 예보 데이터 확인하기
    path("", views.index),
    # 2. 예보 데이터 중 원하는 데이터만 DB에 저장
    path("save-deposit-data/", views.save_deposit_data),
    path("signup_deposit/<int:option_pk>", views.signup_deposit),
    path("deposit_product_list/", views.deposit_product_list),
    path("get_user_grade/", views.get_user_grade),
]

