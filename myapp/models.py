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
    # claim_id = models.IntegerField()
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

    def __int__(self):
        return self.loan_id


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
    turnover_db_20208 = models.CharField(max_length=25, null=True)
    turnover_cr_20208 = models.CharField(max_length=25, null=True)
    turnover_cr_20218 = models.CharField(max_length=25, null=True)
    turnover_db_20218 = models.CharField(max_length=25, null=True)
    turnover_db_20212 = models.CharField(max_length=25, null=True)
    turnover_cr_20212 = models.CharField(max_length=25, null=True)
    saldo_90963 = models.CharField(max_length=25, null=True)

    def __int__(self):
        return self.loan_id


class CreditPayment(models.Model):
    branch_id = models.CharField(max_length=10)
    loan_id = models.IntegerField()
    cl_mfo = models.CharField(max_length=10)
    cl_account = models.CharField(max_length=25)
    cl_name = models.CharField(max_length=255)
    cl_id = models.CharField(max_length=10)
    ca_mfo = models.CharField(max_length=10)
    ca_account = models.CharField(max_length=20)
    ca_name = models.CharField(max_length=255)
    ca_id = models.BigIntegerField()
    doc_id = models.CharField(max_length=10)
    doc_date = models.DateField()
    doc_num = models.IntegerField()
    pay_sum = models.BigIntegerField()
    pay_code = models.CharField(max_length=10)
    pay_note = models.CharField(max_length=200)
    pay_state = models.IntegerField()
    pay_date = models.DateField()

    def __str__(self):
        return self.cl_name


class AddClients(models.Model):
    client_type = models.CharField(max_length=50)
    client_id = models.BigIntegerField()
    client_name = models.CharField(max_length=120)
    nibbd_code = models.CharField(max_length=10)
    doc_date = models.DateField()
    doc_status = models.CharField(max_length=20)
    doc_guid = models.CharField(max_length=100)
    doc_pin = models.CharField(max_length=15)
    credit_sum = models.CharField(max_length=20)
    credit_term = models.IntegerField()
    credit_privilege_month = models.IntegerField()
    doc_num = models.IntegerField()
    credit_percent = models.IntegerField()
    workers = models.IntegerField()
    credit_type = models.CharField(max_length=4)
    region_code = models.IntegerField()
    district_code = models.IntegerField()
    branch_id = models.CharField(max_length=6)
    update_date = models.DateField()
    update_id = models.IntegerField()


    def __str__(self):
        return self.client_name