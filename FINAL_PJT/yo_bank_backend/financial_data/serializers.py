from rest_framework import serializers
from .models import DepositOptions, DepositProduct, SavingOptions, SavingProduct,SubscribedProduct

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductWithOptionsSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProduct
        fields = '__all__'

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'

# class SavingOptionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SavingOptions
#         fields = '__all__'
#         depth = 1  # 관련 SavingProduct의 직렬화를 위해 depth 사용

class SubscribedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedProduct
        fields = '__all__'
        read_only_fields = ['user',]