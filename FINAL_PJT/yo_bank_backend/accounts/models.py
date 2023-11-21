from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username



# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.CharField(max_length=30, unique=True)
    money_for_financial = models.CharField(max_length=30, unique=True)
    money_for_travel = models.CharField(max_length=30, unique=True)
    salary = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    def __str__(self) -> str:
        return self.email



class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        data = form.cleaned_data

        # 기본 필드 처리
        user_email(user, data.get("email"))
        user_username(user, data.get("username"))

        # 선택적인 추가 필드 처리
        self._set_optional_field(user, "money_for_financial", data.get("money_for_financial"))
        self._set_optional_field(user, "money_for_travel", data.get("money_for_travel"))
        self._set_optional_field(user, "nickname", data.get("nickname"))
        self._set_optional_field(user, "age", data.get("age"))
        self._set_optional_field(user, "email", data.get("email"))
        self._set_optional_field(user, "salary", data.get("salary"))

        # financial_products 처리
        financial_product = data.get("financial_products")
        if financial_product:
            self._append_to_csv_field(user, "financial_products", financial_product)

        # 패스워드 처리
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)

        if commit:
            user.save()

        return user

    def _set_optional_field(self, user, field_name, field_value):
        """
        선택적인 필드를 설정합니다.
        """
        if field_value:
            user_field(user, field_name, field_value)

    def _append_to_csv_field(self, user, field_name, value_to_append):
        """
        CSV 필드에 값을 추가합니다.
        """
        current_values = getattr(user, field_name, '').split(',')
        current_values.append(value_to_append)
        
        if len(current_values) > 1:
            updated_value = ','.join(current_values)
            user_field(user, field_name, updated_value)
        else:
            user_field(user, field_name, value_to_append)