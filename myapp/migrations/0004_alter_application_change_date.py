# Generated by Django 4.2.11 on 2024-03-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_application_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='change_date',
            field=models.DateField(null=True),
        ),
    ]
