from django.urls import path
from . import views

urlpatterns = [
    # 1. 날씨 API 테스트 - 서울의 예보 데이터 확인하기
    path("", views.index),
    # 2. 예보 데이터 중 원하는 데이터만 DB에 저장
    path("save-deposit-data/", views.save_deposit_data),
    path("save-saving-data/", views.save_saving_data),
    path("signup_deposit/<int:option_pk>", views.signup_deposit),
    path("signup_saving/<int:option_pk>", views.signup_saving),
    path("deposit_product_list/", views.deposit_product_list),
    path("saving_product_list/", views.saving_product_list),
    path("get_deposit_recommend/", views.get_deposit_recommend),
    path("get_saving_recommend/", views.get_saving_recommend),
    path("get_my_subscribed/", views.get_my_subscribed),
    path("delete_product/<int:subscribed_pk>", views.delete_product),
    path("get_my_deposit/", views.get_my_deposit),
    # path("subcribed_list/", views.subcribed_list),
    # path("delete_product/<int:subscribed_pk>", views.delete_product),
]

