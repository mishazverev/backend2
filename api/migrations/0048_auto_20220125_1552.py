# Generated by Django 3.2.11 on 2022-01-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20220124_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontractonetimefee',
            name='rent_contract_additional_agreement_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement'),
        ),
        migrations.AlterField(
            model_name='rentcontractperiodicalfee',
            name='rent_contract_additional_agreement_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement'),
        ),
        migrations.AlterField(
            model_name='rentcontractutilityfee',
            name='rent_contract_additional_agreement_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement'),
        ),
    ]
