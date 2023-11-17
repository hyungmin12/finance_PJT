from django.db import models


class Deposit(models.Model):
    dcls_month = models.CharField(max_length=50)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_cd = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=50)
    join_way = models.CharField(max_length=50)
    mtrt_int = models.CharField(max_length=300)
    spcl_cnd = models.CharField(max_length=300)
    join_member = models.CharField(max_length=300)
    etc_note = models.CharField(max_length=300)
    dcls_strt_day = models.CharField(max_length=50)
    fin_co_subm_day = models.CharField(max_length=50)
    intr_rate_type = models.CharField(max_length=300)
    intr_rate_type_nm = models.CharField(max_length=300)
    save_trm = models.CharField(max_length=300)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()

class Exchange(models.Model):
    pass