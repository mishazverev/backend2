# Generated by Django 3.2.6 on 2022-01-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20211218_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontract',
            name='CA_utilities_compensation_fee_payment_day',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_payment_day',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_payment_day',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='utilities_gas_compensation_payment_day',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_payment_day',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
