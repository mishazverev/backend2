# Generated by Django 3.2.11 on 2022-02-17 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0062_auto_20220217_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalAgreement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('additional_agreement_number', models.CharField(max_length=50)),
                ('additional_agreement_signing_date', models.DateField(blank=True, null=True)),
                ('additional_agreement_expiration_date', models.DateField(blank=True, null=True)),
                ('contracted_area', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('act_of_transfer_date', models.DateField(blank=True, null=True)),
                ('rent_start_date', models.DateField(blank=True, null=True)),
                ('premise_return_date', models.DateField(blank=True, null=True)),
                ('stop_billing_date', models.DateField(blank=True, null=True)),
                ('fixed_rent_calculation_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('fixed_rent_payment_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('fixed_rent_per_sqm', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('fixed_rent_total_payment', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('fixed_rent_advance_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('fixed_rent_post_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('fixed_rent_indexation_type', models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('fixed_rent_indexation_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('turnover_fee', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('turnover_fee_period', models.CharField(blank=True, choices=[('1_month', 'Month1'), ('3_months', 'Month3'), ('6_months', 'Month6'), ('12_months', 'Month12')], default='1_month', max_length=20, null=True)),
                ('turnover_data_providing_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('turnover_fee_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('CA_utilities_compensation_type', models.CharField(choices=[('Fixed', 'Fixed'), ('Proportional_to_GLA', 'Proportional Gla'), ('Proportional_to_leased area', 'Proportional Leased'), ('None', 'None')], default='Proportional_to_GLA', max_length=50, null=True)),
                ('CA_utilities_compensation_fixed_indexation_type', models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('CA_utilities_compensation_fee_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('CA_utilities_compensation_fee_fixed_indexation_type_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('CA_utilities_compensation_fee_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('guarantee_deposit_required', models.BooleanField(default=True)),
                ('guarantee_deposit_coverage_number_of_periods', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('guarantee_deposit_type', models.CharField(choices=[('Cash', 'Cash'), ('Bank guarantee', 'Bank Guarantee'), ('Corporate guarantee', 'Corporate Guarantee')], default='Cash', max_length=25, null=True)),
                ('guarantee_deposit_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('guarantee_deposit_contract_providing_date', models.DateField(null=True)),
                ('guarantee_deposit_actual_providing_date', models.DateField(null=True)),
                ('guarantee_bank_guarantee_expiration_date', models.DateField(null=True)),
                ('insurance_required', models.BooleanField(default=True)),
                ('insurance_contract_providing_date', models.DateField(blank=True, null=True)),
                ('insurance_actual_providing_date', models.DateField(blank=True, null=True)),
                ('insurance_expiration_date', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.brand')),
                ('premise_id', models.ManyToManyField(to='api.PremiseMain')),
            ],
            options={
                'ordering': ['additional_agreement_number'],
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('counter_number', models.CharField(max_length=50, unique=True)),
                ('counter_utility_type', models.CharField(max_length=50, unique=True)),
                ('counter_description', models.CharField(blank=True, max_length=200, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['counter_number'],
            },
        ),
        migrations.CreateModel(
            name='RentContract',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rent_contract_number', models.CharField(max_length=50)),
                ('rent_contract_signing_date', models.DateField(blank=True, null=True)),
                ('rent_contract_expiration_date', models.DateField(blank=True, null=True)),
                ('contracted_area', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('act_of_transfer_date', models.DateField(blank=True, null=True)),
                ('rent_start_date', models.DateField(blank=True, null=True)),
                ('premise_return_date', models.DateField(blank=True, null=True)),
                ('stop_billing_date', models.DateField(blank=True, null=True)),
                ('fixed_rent_name', models.CharField(blank=True, max_length=100, null=True)),
                ('fixed_rent_calculation_period', models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('fixed_rent_payment_period', models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('fixed_rent_calculation_method', models.CharField(blank=True, choices=[('Per_sqm', 'Per Sqm'), ('Total', 'Total')], default='Per_sqm', max_length=20, null=True)),
                ('fixed_rent_per_sqm', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('fixed_rent_total_payment', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('fixed_rent_prepayment_or_postpayment', models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True)),
                ('fixed_rent_advance_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('fixed_rent_post_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('fixed_rent_indexation_type', models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('fixed_rent_indexation_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('turnover_fee_is_applicable', models.BooleanField(default=True)),
                ('turnover_fee', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('turnover_fee_period', models.CharField(blank=True, choices=[('1_month', 'Month1'), ('3_months', 'Month3'), ('6_months', 'Month6'), ('12_months', 'Month12')], default='1_month', max_length=20, null=True)),
                ('turnover_data_providing_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('turnover_fee_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('CA_utilities_compensation_is_applicable', models.BooleanField(default=True)),
                ('CA_utilities_compensation_type', models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('Proportional_to_GLA', 'Proportional Gla'), ('Proportional_to_leased area', 'Proportional Leased'), ('None', 'None')], default='Proportional_to_GLA', max_length=50, null=True)),
                ('CA_utilities_compensation_fixed_indexation_type', models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('CA_utilities_compensation_fee_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('CA_utilities_compensation_fee_fixed_indexation_type_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('CA_utilities_compensation_fee_prepayment_or_postpayment', models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True)),
                ('CA_utilities_compensation_fee_advance_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('CA_utilities_compensation_fee_post_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('guarantee_deposit_required', models.BooleanField(default=True)),
                ('guarantee_deposit_coverage_number_of_periods', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('guarantee_deposit_type', models.CharField(choices=[('Cash', 'Cash'), ('Bank guarantee', 'Bank Guarantee'), ('Corporate guarantee', 'Corporate Guarantee')], default='Cash', max_length=25, null=True)),
                ('guarantee_deposit_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('guarantee_deposit_contract_providing_date', models.DateField(null=True)),
                ('guarantee_deposit_actual_providing_date', models.DateField(null=True)),
                ('guarantee_bank_guarantee_expiration_date', models.DateField(null=True)),
                ('insurance_required', models.BooleanField(default=True)),
                ('insurance_contract_providing_date', models.DateField(blank=True, null=True)),
                ('insurance_actual_providing_date', models.DateField(blank=True, null=True)),
                ('insurance_expiration_date', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.brand')),
                ('building_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.building')),
                ('premise_id', models.ManyToManyField(to='api.PremiseMain')),
                ('tenant_contractor_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.tenantcontractor')),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rent_contract_number'],
            },
        ),
        migrations.CreateModel(
            name='RentContractUtilityFee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('utility_name', models.CharField(max_length=100)),
                ('compensation_type', models.CharField(choices=[('Using counter', 'Using Counter'), ('Fixed', 'Fixed'), ('None', 'None')], default='Using counter', max_length=20, null=True)),
                ('compensation_calculation_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('compensation_payment_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('compensation_fixed_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('compensation_fixed_fee_indexation_type', models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('compensation_fixed_fee_indexation_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('compensation_advance_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('compensation_counter_data_providing_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('compensation_post_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('counter_id', models.ManyToManyField(to='api.Counter')),
                ('rent_contract_additional_agreement_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement')),
                ('rent_contract_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rentcontract')),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['utility_name'],
            },
        ),
        migrations.CreateModel(
            name='RentContractPeriodicalFee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('periodical_fee_name', models.CharField(max_length=100)),
                ('periodical_fee_calculation_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('periodical_fee_payment_period', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True)),
                ('periodical_fee_calculation_method', models.CharField(choices=[('Per_sqm', 'Per Sqm'), ('Total', 'Total')], default='Per_sqm', max_length=20, null=True)),
                ('periodical_fee_per_sqm', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('periodical_fee_total_payment', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('periodical_fee_advance_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('periodical_fee_post_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('periodical_fee_indexation_type', models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True)),
                ('periodical_payment_indexation_fixed', models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent_contract_additional_agreement_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement')),
                ('rent_contract_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rentcontract')),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['periodical_fee_name'],
            },
        ),
        migrations.CreateModel(
            name='RentContractOneTimeFee',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('one_time_fee_name', models.CharField(max_length=100)),
                ('one_time_fee_calculation_method', models.CharField(choices=[('Per_sqm', 'Per Sqm'), ('Total', 'Total')], default='Per_sqm', max_length=20, null=True)),
                ('one_time_fee_payment_term', models.CharField(choices=[('Fixed_date', 'Fixed Date'), ('Triggering_event_date', 'Triggering Event Date'), ('Not_fixed', 'Not Fixed')], default='Fixed_date', max_length=50, null=True)),
                ('one_time_fee_payment_triggering_event', models.CharField(choices=[('Contract_signing_date', 'Contract Signing Date'), ('Premise_transfer_date', 'Act Of Transfer Date'), ('Start_of_commercial_activity', 'Rent Start Date')], default='Premise_transfer_date', max_length=50, null=True)),
                ('one_time_fee_per_sqm', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('one_time_fee_total_payment', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('one_time_fee_contract_payment_date', models.DateField(blank=True, null=True)),
                ('one_time_fee_contract_triggering_event_related_payment_day', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent_contract_additional_agreement_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.additionalagreement')),
                ('rent_contract_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rentcontract')),
                ('user_updated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['one_time_fee_name'],
            },
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='rent_contract_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.rentcontract'),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='tenant_contractor_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.tenantcontractor'),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='user_updated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
