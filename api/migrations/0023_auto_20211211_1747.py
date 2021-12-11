# Generated by Django 3.2.6 on 2021-12-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20211211_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentcontract',
            name='act_of_transfer_signed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='duration_days',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='duration_months',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='duration_years',
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='contract_expiration_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='premise_return_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='stop_billing_date',
            field=models.DateField(null=True),
        ),
    ]
