# Generated by Django 4.2.4 on 2023-08-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egrn_info', '0002_rename_name_entity_full_name_entity_activity_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='pan',
            field=models.PositiveIntegerField(unique=True, verbose_name='Регистрационный номер'),
        ),
    ]
