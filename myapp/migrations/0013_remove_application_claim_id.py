# Generated by Django 4.2.11 on 2024-04-17 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_creditpay_account_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='claim_id',
        ),
    ]