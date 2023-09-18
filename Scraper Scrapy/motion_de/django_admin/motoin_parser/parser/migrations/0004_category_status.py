# Generated by Django 4.2.2 on 2023-07-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('status1', 'Not started'), ('status2', 'Finished'), ('status3', 'Finished with error')], default='status1', max_length=15, verbose_name='Статус'),
        ),
    ]
