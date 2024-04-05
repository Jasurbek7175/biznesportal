from django.db import models
import uuid


# Create your models here.


class Application(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    mfo = models.CharField(max_length=5)
    branch_id = models.CharField(max_length=5)
    application_id = models.IntegerField()
    loan_id = models.IntegerField()
    state = models.CharField(max_length=255)
    claim_id = models.IntegerField()
    region_code = models.CharField(max_length=5)
    district_code = models.CharField(max_length=5)
    client_type = models.CharField(max_length=20)
    client_name = models.CharField(max_length=255)
    client_id = models.BigIntegerField()
    credit_sum = models.BigIntegerField()
    credit_percent = models.FloatField()
    credit_date = models.DateField()
    change_date = models.DateField(null=True)
    credit_term_date = models.DateField(null=True)
    credit_num = models.CharField(max_length=15, null=True)
    credit_purpose_code = models.CharField(max_length=20, null=True)
    credit_purpose_name = models.CharField(max_length=255, null=True)
    credit_account = models.CharField(max_length=25, null=True)
    overdue_debt_account = models.CharField(max_length=25, null=True)
    first_pay_date = models.DateField(null=True)
    last_pay_date = models.DateField(null=True)
    total_pay_sum = models.BigIntegerField(null=True)
    debt_sum = models.BigIntegerField(null=True)
    overdue_debt_sum = models.FloatField(null=True)
    overdue_debt_date = models.DateField(null=True)
    overdue_debt_day = models.IntegerField(null=True)
    next_month_pay_sum = models.FloatField(null=True)
    account_16309_sum = models.CharField(max_length=25, null=True)
    account_16323_sum = models.CharField(max_length=25, null=True)
    account_16377_sum = models.CharField(max_length=25, null=True)
    account_16379_sum = models.CharField(max_length=25, null=True)
    account_16405_sum = models.CharField(max_length=25, null=True)
    account_16413_sum = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.claim_id


class ClientInfo(models.Model):
    request_id = models.CharField(max_length=255)
    application_id = models.IntegerField()

    def __str__(self):
        return self.request_id


class CreditPay(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    loan_id = models.IntegerField()
    nibbd_code = models.CharField(max_length=12)
    mfo = models.CharField(max_length=6)
    account = models.CharField(max_length=25)
    branch_id = models.CharField(max_length=10)
    account_status = models.IntegerField()
    turnover_db_20208 = models.BigIntegerField(null=True)
    turnover_cr_20208 = models.BigIntegerField(null=True)
    turnover_cr_20218 = models.BigIntegerField(null=True)
    turnover_db_20218 = models.BigIntegerField(null=True)
    turnover_cr_22618 = models.BigIntegerField(null=True)
    turnover_db_22618 = models.BigIntegerField(null=True)
    turnover_db_20212 = models.BigIntegerField(null=True)
    turnover_cr_20212 = models.BigIntegerField(null=True)
    saldo_90963 = models.BigIntegerField(null=True)

    def __str__(self):
        return self.loan_id
