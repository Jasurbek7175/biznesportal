# Generated by Django 4.2.11 on 2024-03-15 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='district_id',
            new_name='district_code',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='region_id',
            new_name='region_code',
        ),
    ]
