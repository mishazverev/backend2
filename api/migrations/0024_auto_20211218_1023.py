# Generated by Django 3.2.6 on 2021-12-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20211211_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_compensation_fixed_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_compensation_fixed_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_compensation_fixed_payment_day',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_compensation_type',
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='turnover_data_providing_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='turnover_fee_payment_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='turnover_fee_period',
            field=models.CharField(choices=[('1_month', 'Month 1'), ('3_months', 'Months 3'), ('6_months', 'Months 6'), ('12_months', 'Months 12')], default='1_month', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_fixed_indexation_fixed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_payment_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_type',
            field=models.CharField(choices=[('By counters', 'By Counters'), ('Fixed', 'Fixed'), ('None', 'None')], default='By counters', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_cold_water_counter_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_fixed_indexation_fixed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_payment_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_type',
            field=models.CharField(choices=[('By counters', 'By Counters'), ('Fixed', 'Fixed'), ('None', 'None')], default='By counters', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_electricity_counter_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_gas_compensation_fixed_indexation_fixed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_gas_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_gas_compensation_payment_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_gas_compensation_type',
            field=models.CharField(choices=[('By counters', 'By Counters'), ('Fixed', 'Fixed'), ('None', 'None')], default='By counters', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_gas_counter_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_fixed_indexation_fixed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_payment_day',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_type',
            field=models.CharField(choices=[('By counters', 'By Counters'), ('Fixed', 'Fixed'), ('None', 'None')], default='By counters', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='utilities_hot_water_counter_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
