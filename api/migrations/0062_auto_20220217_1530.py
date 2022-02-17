# Generated by Django 3.2.11 on 2022-02-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_auto_20220217_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='user_updated',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='building_id',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='premise_id',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='tenant_contractor_id',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='user_updated',
        ),
        migrations.RemoveField(
            model_name='rentcontractonetimefee',
            name='rent_contract_additional_agreement_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractonetimefee',
            name='rent_contract_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractonetimefee',
            name='user_updated',
        ),
        migrations.RemoveField(
            model_name='rentcontractperiodicalfee',
            name='rent_contract_additional_agreement_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractperiodicalfee',
            name='rent_contract_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractperiodicalfee',
            name='user_updated',
        ),
        migrations.RemoveField(
            model_name='rentcontractutilityfee',
            name='counter_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractutilityfee',
            name='rent_contract_additional_agreement_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractutilityfee',
            name='rent_contract_id',
        ),
        migrations.RemoveField(
            model_name='rentcontractutilityfee',
            name='user_updated',
        ),
        migrations.DeleteModel(
            name='AdditionalAgreement',
        ),
        migrations.DeleteModel(
            name='Counter',
        ),
        migrations.DeleteModel(
            name='RentContract',
        ),
        migrations.DeleteModel(
            name='RentContractOneTimeFee',
        ),
        migrations.DeleteModel(
            name='RentContractPeriodicalFee',
        ),
        migrations.DeleteModel(
            name='RentContractUtilityFee',
        ),
    ]
