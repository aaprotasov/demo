# Generated by Django 4.2.4 on 2023-08-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egrn_info', '0004_alter_entity_email_alter_entity_fio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='activity_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='вид деятельности'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='fio',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='full_name',
            field=models.CharField(max_length=500, verbose_name='Наименование юр. лица'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='full_name_bel',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Наименование юр. лица (бел)'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='registration_authority',
            field=models.CharField(max_length=500, verbose_name='Регистрирующий орган'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='registration_place',
            field=models.CharField(max_length=500, verbose_name='Место регистрации'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='short_name',
            field=models.CharField(max_length=500, null=True, verbose_name='Краткое наименование'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='short_name_bel',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Краткое наименование (бел)'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='state',
            field=models.CharField(max_length=500, verbose_name='Статус'),
        ),
    ]
