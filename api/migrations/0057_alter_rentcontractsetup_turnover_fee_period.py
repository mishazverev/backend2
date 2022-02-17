# Generated by Django 3.2.11 on 2022-02-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20220212_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontractsetup',
            name='turnover_fee_period',
            field=models.CharField(blank=True, choices=[('Month', 'Month1'), ('3_months', 'Month3'), ('6_months', 'Month6'), ('Year', 'Month12')], default='Month', max_length=20, null=True),
        ),
    ]