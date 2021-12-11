# Generated by Django 3.2.6 on 2021-12-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20211123_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontract',
            name='CA_utilities_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='marketing_fee_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='rent_fee_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='CPI', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='service_fee_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rentcontract',
            name='utilities_compensation_fixed_indexation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('CPI', 'Cpi'), ('Revisable', 'Revisable'), ('NonIndexable', 'Nonindexable')], default='Fixed', max_length=20, null=True),
        ),
    ]