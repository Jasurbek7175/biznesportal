# Generated by Django 4.2.11 on 2024-05-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_creditpay_turnover_cr_22618_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(max_length=50)),
                ('client_id', models.BigIntegerField()),
                ('client_name', models.CharField(max_length=120)),
                ('nibbd_code', models.CharField(max_length=10)),
                ('doc_date', models.DateField()),
                ('doc_status', models.CharField(max_length=20)),
                ('doc_guid', models.CharField(max_length=100)),
                ('doc_pin', models.CharField(max_length=15)),
                ('credit_sum', models.CharField(max_length=20)),
                ('credit_term', models.IntegerField()),
                ('credit_privilege_month', models.IntegerField()),
                ('credit_percent', models.IntegerField()),
                ('workers', models.IntegerField()),
                ('credit_type', models.CharField(max_length=4)),
                ('region_code', models.IntegerField()),
                ('district_code', models.IntegerField()),
                ('branch_id', models.CharField(max_length=6)),
                ('update_date', models.DateField()),
                ('update_id', models.IntegerField()),
            ],
        ),
    ]