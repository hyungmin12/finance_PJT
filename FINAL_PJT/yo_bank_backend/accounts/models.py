from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username



# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(default=0)
    used_money_for_financial = models.IntegerField(default=0)
    left_money_for_financial = models.IntegerField(default=1)
    money_for_financial = models.IntegerField(default=0)
    money_for_travel = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    financial_products = models.TextField(blank=True, null=True)
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
        nickname = data.get("nickname")
        age = data.get("age")
        money_for_financial = data.get("money_for_financial")
        money_for_travel = data.get("money_for_travel")
        financial_product = data.get("financial_products")
        used_money_for_financial = data.get("used_money_for_financial") or 0
        left_money_for_financial = data.get("left_money_for_financial") or 1
        salary = data.get("salary")
        user_email(user, email)
        user_username(user, username)
        user.age = age
        user.money_for_financial = money_for_financial
        user.money_for_travel = money_for_travel
        user.nickname = nickname
        user.salary = salary
        user.left_money_for_financial = left_money_for_financial
        user.used_money_for_financial = used_money_for_financial
        user.financial_product = financial_product
        # user_field(user, "salary", salary)
        
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