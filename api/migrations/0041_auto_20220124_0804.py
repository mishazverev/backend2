# Generated by Django 3.2.11 on 2022-01-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_rentcontractutilityfeesetup_compensation_fixed_fee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryTag',
            new_name='BrandCategoryTag',
        ),
        migrations.RenameField(
            model_name='rentcontractutilityfee',
            old_name='counter_numbers',
            new_name='counter_id',
        ),
        migrations.AddField(
            model_name='building',
            name='building_name',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]
