# Generated by Django 4.2 on 2023-07-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_info_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='vaccine_total_doses',
            field=models.IntegerField(default=1),
        ),
    ]
