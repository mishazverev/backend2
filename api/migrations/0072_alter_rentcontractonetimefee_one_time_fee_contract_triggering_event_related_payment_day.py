# Generated by Django 3.2.11 on 2022-03-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_remove_rentcontractutilityfee_counter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontractonetimefee',
            name='one_time_fee_contract_triggering_event_related_payment_day',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True),
        ),
    ]
