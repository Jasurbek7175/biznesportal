# Generated by Django 4.2.11 on 2024-03-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_application_loan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='debt_sum',
            field=models.BigIntegerField(null=True),
        ),
    ]