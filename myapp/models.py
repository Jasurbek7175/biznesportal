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
    state = models.CharField(max_length=255)
    claim_id = models.IntegerField()
    region_code = models.CharField(max_length=5)
    district_code = models.CharField(max_length=5)
    client_type = models.CharField(max_length=20)
    client_name = models.CharField(max_length=255)
    client_id = models.BigIntegerField()
    credit_sum = models.FloatField()
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
    total_pay_sum = models.FloatField(null=True)
    debt_sum = models.FloatField(null=True)
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

