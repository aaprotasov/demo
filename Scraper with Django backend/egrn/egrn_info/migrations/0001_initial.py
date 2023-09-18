# Generated by Django 4.2.4 on 2023-08-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование юр. лица')),
                ('pan', models.IntegerField(verbose_name='Регистрационный номер')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронный адрес')),
                ('phone_number', models.CharField(blank=True, verbose_name='Телефон')),
                ('state', models.CharField(max_length=30, verbose_name='Статус')),
                ('registration_authority', models.CharField(max_length=100, verbose_name='Регистрирующий орган')),
                ('registration_place', models.CharField(max_length=100, verbose_name='Место регистрации')),
                ('registration_date', models.DateTimeField(verbose_name='Дата регистрации')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое наименование')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'db_table': 'entity',
            },
        ),
    ]