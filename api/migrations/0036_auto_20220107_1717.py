# Generated by Django 3.2.6 on 2022-01-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20220106_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentcontract',
            name='advance_payment_amount',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='advance_payment_contract_providing_date',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='advance_payment_paid',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='advance_payment_required',
        ),
    ]
