# Generated by Django 4.2.11 on 2024-04-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_creditpay_delete_informationapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditpay',
            name='account_status',
            field=models.IntegerField(),
        ),
    ]
