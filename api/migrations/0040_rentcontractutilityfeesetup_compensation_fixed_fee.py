# Generated by Django 3.2.11 on 2022-01-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20220115_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentcontractutilityfeesetup',
            name='compensation_fixed_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
