from rest_framework import serializers
from .models import Application


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "mfo",
            "branch_id",
            "application_id",
            "state",
            "claim_id",
            "region_code",
            "district_code",
            "client_type",
            "client_name",
            "client_id",
            "credit_sum",
            "credit_percent",
            "credit_date",
            "change_date",
            "credit_term_date",
            "credit_num",
            "credit_purpose_code",
            "credit_purpose_name",
            "credit_account",
            "overdue_debt_account",
            "first_pay_date",
            "last_pay_date",
            "total_pay_sum",
            "debt_sum",
            "overdue_debt_sum",
            "overdue_debt_date",
            "overdue_debt_day",
            "next_month_pay_sum",
            "account_16309_sum",
            "account_16323_sum",
            "account_16377_sum",
            "account_16379_sum",
            "account_16405_sum",
            "account_16413_sum",
        ]
