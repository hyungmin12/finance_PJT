from django.db import models
from accounts.models import User

# Create your models here.


#예금
class DepositProduct(models.Model):
    # 금융회사 코드
    fin_co_no = models.TextField(null=True)
    # 금융상품코드
    fin_prdt_cd = models.TextField(null=True,unique=True)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입대상
    join_member = models.TextField(null=True)
    # 가입방법
    join_way = models.TextField(null=True)
    # 우대조건
    spcl_cnd = models.TextField(null=True)
    # 최고한도
    max_limit = models.IntegerField(null=True)
    #기타 유의사항
    etc_note = models.TextField(null=True)
    #공시 종료일
    dcls_end_day = models.TextField(null=True)


class DepositOptions(models.Model):
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE, related_name='options', to_field='fin_prdt_cd')
    intr_rate_type = models.TextField(null=True)
    intr_rate_type_nm = models.TextField(null=True)
    save_trm = models.IntegerField(null=True)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

    def __str__(self):
        return f"{self.deposit_product.fin_prdt_cd} - {self.intr_rate_type}"


# class DepositOptions(models.Model):
#     # 금융상품코드
#     fin_prdt_cd = models.TextField(null=True)
#     # 저축금리유형
#     intr_rate_type = models.TextField(null=True)
#     # 저축금리유형명
#     intr_rate_type_nm = models.TextField(null=True)
#     # 저축기간(개월)
#     save_trm = models.IntegerField(null=True)
#     # 저축금리
#     intr_rate = models.FloatField(null=True)
#     # 최고우대금리
#     intr_rate2 = models.FloatField(null=True)

class SavingProduct(models.Model):
    # 금융상품코드
    fin_prdt_cd = models.TextField(null=True,unique=True)
    # 금융회사코드
    fin_co_no = models.TextField(null=True)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융상품명
    fin_prdt_nm = models.TextField(null=True)
    # 가입제한
    join_deny = models.IntegerField(null=True)
    # 가입대상
    join_member = models.TextField(null=True)
    # 가입방법
    join_way = models.TextField(null=True)
    # 우대조건
    spcl_cnd = models.TextField(null=True)
    # 최고한도
    max_limit = models.IntegerField(null=True)
    # 기타 유의사항
    etc_note = models.TextField(null=True)
    # 공시 종료일
    dcls_end_day = models.TextField(null=True)

class SavingOptions(models.Model):
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE, related_name='options', to_field='fin_prdt_cd')
    # 저축금리유형
    intr_rate_type = models.TextField(null=True)
    # 저축금리유형명
    intr_rate_type_nm = models.TextField(null=True)
    # 적립유형
    rsrv_type = models.TextField(null=True)
    # 적립유형명
    rsrv_type_nm = models.TextField(null=True)
    # 저축기간(개월)
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고우대금리
    intr_rate2 = models.FloatField(null=True)


class SubscribedProduct(models.Model):
    # 가입한 유저
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    # 종류(적금인지 예금인지)
    type = models.TextField(null=True)
    # 금융상품코드
    fin_prdt_cd = models.TextField(null=True)
    # 금융회사명
    kor_co_nm = models.TextField(null=True)
    # 금융상품명
    fin_prdt_nm = models.TextField(null=True)
    # 최고한도
    max_limit = models.IntegerField(null=True)
    # 가입액
    amount = models.IntegerField()
    #공시 종료일
    dcls_end_day = models.TextField(null=True)
    # 적립유형
    rsrv_type = models.TextField(null=True)
    # 적립유형명
    rsrv_type_nm = models.TextField(null=True)
    # 저축금리유형
    intr_rate_type = models.TextField(null=True)
    # 저축금리유형명
    intr_rate_type_nm = models.TextField(null=True)
    # 저축기간(개월)
    save_trm = models.IntegerField(null=True)
    # 저축금리
    intr_rate = models.FloatField(null=True)
    # 최고우대금리
    intr_rate2 = models.FloatField(null=True)




# class SubscribedSaving(models.Model):
#         # 가입한 유저
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # 금융상품코드
#     fin_prdt_cd = models.TextField(null=True)
#     # 금융회사명
#     kor_co_nm = models.TextField(null=True)
#     # 금융상품명
#     fin_prdt_nm = models.TextField(null=True)
#     # 최고한도
#     max_limit = models.IntegerField(null=True)
#     # 가입액
#     saving_amount = models.IntegerField()
#     #공시 종료일
#     dcls_end_day = models.TextField(null=True)
#     # 적립유형
#     rsrv_type = models.TextField(null=True)
#     # 적립유형명
#     rsrv_type_nm = models.TextField(null=True)
#     # 저축금리유형
#     intr_rate_type = models.TextField(null=True)
#     # 저축금리유형명
#     intr_rate_type_nm = models.TextField(null=True)
#     # 저축기간(개월)
#     save_trm = models.IntegerField(null=True)
#     # 저축금리
#     intr_rate = models.FloatField(null=True)
#     # 최고우대금리
#     intr_rate2 = models.FloatField(null=True)