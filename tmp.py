from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    campus = models.CharField(max_length=10)
    generation = models.IntegerField(null=False)
    salary = models.IntegerField()
    fi_money = models.IntegerField(default=0)  # 현재 상품에 넣고 있는 금액
    fixed_cost = models.IntegerField(default=0) # 고정 지출
    rent_help = models.BooleanField(default=False) # 월세 지원
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        campus = data.get("campus")
        generation = str(data.get("generation"))
        rent_help = data.get("rent_help")
        financial_product = data.get("financial_products")
        user_email(user, email)
        user_username(user, username)
        user.campus = campus
        user.generation = generation
        user.rent_help = rent_help
        salary = 1000000
        if campus != '서울':
            salary += 300000
        if rent_help:
            salary += 200000
        # user_field(user, "salary", salary)
        user.salary = salary
        
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)

            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user