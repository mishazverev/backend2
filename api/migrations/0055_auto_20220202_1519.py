# Generated by Django 3.2.11 on 2022-02-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_remove_rentcontractsetup_fixed_rent_calculation_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentcontractperiodicalfeesetup',
            name='periodical_fee_prepayment_or_postpayment',
            field=models.CharField(choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontractutilityfeesetup',
            name='compensation_fixed_fee_prepayment_or_postpayment',
            field=models.CharField(choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
    ]
