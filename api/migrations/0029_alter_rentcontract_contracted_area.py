# Generated by Django 3.2.6 on 2022-01-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20220103_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcontract',
            name='contracted_area',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
