from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model



class CustomRegisterSerializer(RegisterSerializer):
# 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    money_for_financial = serializers.IntegerField(required=False)
    money_for_travel = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.CharField(), required=False)
    
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'email' : self.validated_data.get('email', ''),
        'age': self.validated_data.get('age', ''),
        'money_for_financial': self.validated_data.get('money_for_financial', ''),
        'money_for_travel': self.validated_data.get('money_for_travel', ''),
        'salary': self.validated_data.get('salary', ''),
        'financial_products': self.validated_data.get('financial_products', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = ('id','email','username','nickname','money_for_financial','money_for_travel','age','used_money_for_financial','left_money_for_financial','salary')


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'