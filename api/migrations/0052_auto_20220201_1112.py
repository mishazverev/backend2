# Generated by Django 3.2.11 on 2022-02-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_rentcontractsetup_fixed_rent_prepayment_or_postpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentcontractsetup',
            name='CA_utilities_compensation_is_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rentcontractsetup',
            name='turnover_fee_is_applicable',
            field=models.BooleanField(default=True),
        ),
    ]
