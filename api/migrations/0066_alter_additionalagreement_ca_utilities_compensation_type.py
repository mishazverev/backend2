# Generated by Django 3.2.11 on 2022-02-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20220221_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalagreement',
            name='CA_utilities_compensation_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Proportional_to_GLA', 'Proportional Gla'), ('Proportional_to_leased_area', 'Proportional Leased'), ('None', 'None')], default='Proportional_to_GLA', max_length=50, null=True),
        ),
    ]