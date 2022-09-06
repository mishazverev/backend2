# Generated by Django 3.2.11 on 2022-09-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_fixedrentindexationstep_periodicalfeeindexationstep_turnoverfeestep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalagreement',
            old_name='CA_utilities_compensation_fee_payment_day',
            new_name='CA_utilities_compensation_fee_advance_payment_day',
        ),
        migrations.RenameField(
            model_name='additionalagreement',
            old_name='act_of_transfer_date',
            new_name='rent_contract_expiration_date',
        ),
        migrations.RemoveField(
            model_name='additionalagreement',
            name='premise_return_date',
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_fee_post_payment_day',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_fee_prepayment_or_postpayment',
            field=models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_is_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='fixed_rent_calculation_method',
            field=models.CharField(blank=True, choices=[('Per_sqm', 'Per Sqm'), ('Total', 'Total')], default='Per_sqm', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='fixed_rent_prepayment_or_postpayment',
            field=models.CharField(blank=True, choices=[('Prepayment', 'Prepayment'), ('Postpayment', 'Postpayment')], default='Prepayment', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='additionalagreement',
            name='turnover_fee_is_applicable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_fixed_indexation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('Proportional_to_GLA', 'Proportional Gla'), ('Proportional_to_leased_area', 'Proportional Leased'), ('None', 'None')], default='Proportional_to_GLA', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='fixed_rent_calculation_period',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='fixed_rent_indexation_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('Non_Indexable', 'Non Indexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='fixed_rent_payment_period',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='guarantee_deposit_type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank_guarantee', 'Bank Guarantee'), ('Corporate_guarantee', 'Corporate Guarantee')], default='Cash', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='turnover_fee_period',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('3_months', 'Months3'), ('6_months', 'Months6'), ('Year', 'Year')], default='Month', max_length=20, null=True),
        ),
    ]
