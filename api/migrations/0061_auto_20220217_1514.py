# Generated by Django 3.2.11 on 2022-02-17 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_alter_rentcontractsetup_ca_utilities_compensation_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentcontract',
            options={'ordering': ['rent_contract_number']},
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='CA_utilities_compensation_fee_payment_day',
            new_name='CA_utilities_compensation_fee_advance_payment_day',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='marketing_fee_advance_payment_day',
            new_name='CA_utilities_compensation_fee_post_payment_day',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='rent_fee_advance_payment_day',
            new_name='fixed_rent_advance_payment_day',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='marketing_fee_indexation_fixed',
            new_name='fixed_rent_indexation_fixed',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='utilities_cold_water_counter_number',
            new_name='fixed_rent_name',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='marketing_fee_per_sqm',
            new_name='fixed_rent_per_sqm',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='service_fee_advance_payment_day',
            new_name='fixed_rent_post_payment_day',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='service_fee_per_sqm',
            new_name='fixed_rent_total_payment',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='contract_expiration_date',
            new_name='insurance_actual_providing_date',
        ),
        migrations.RenameField(
            model_name='rentcontract',
            old_name='contract_signing_date',
            new_name='rent_contract_expiration_date',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='guarantee_deposit_provided',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='insurance_provided',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='marketing_fee_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='rent_fee_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='rent_fee_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='rent_fee_per_sqm',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='service_fee_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='service_fee_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_fixed_fee',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_fixed_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_fixed_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_payment_day',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_cold_water_compensation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_fixed_fee',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_fixed_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_fixed_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_payment_day',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_compensation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_electricity_counter_number',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_compensation_fixed_fee',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_compensation_fixed_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_compensation_fixed_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_compensation_payment_day',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_compensation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_gas_counter_number',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_fixed_fee',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_fixed_indexation_fixed',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_fixed_indexation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_payment_day',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_compensation_type',
        ),
        migrations.RemoveField(
            model_name='rentcontract',
            name='utilities_hot_water_counter_number',
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='CA_utilities_compensation_fee_prepayment_or_postpayment',
            field=models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='CA_utilities_compensation_is_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='building_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.building'),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='fixed_rent_calculation_method',
            field=models.CharField(blank=True, choices=[('Per_sqm', 'Per Sqm'), ('Total', 'Total')], default='Per_sqm', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='fixed_rent_calculation_period',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='fixed_rent_indexation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='fixed_rent_payment_period',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='fixed_rent_prepayment_or_postpayment',
            field=models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='guarantee_deposit_actual_providing_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='guarantee_deposit_coverage_number_of_periods',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='guarantee_deposit_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='rent_contract_signing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rentcontract',
            name='turnover_fee_is_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='CA_utilities_compensation_fixed_indexation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='CA_utilities_compensation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('Proportional_to_GLA', 'Proportional Gla'), ('Proportional_to_leased area', 'Proportional Leased'), ('None', 'None')], default='Proportional_to_GLA', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='guarantee_deposit_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank guarantee', 'Bank Guarantee'), ('Corporate guarantee', 'Corporate Guarantee')], default='Cash', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='insurance_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='rent_contract_number',
            field=models.CharField(default=-11, max_length=50),
            preserve_default=False,
        ),
    ]