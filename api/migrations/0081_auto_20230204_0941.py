# Generated by Django 3.2.11 on 2023-02-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0080_auto_20220906_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='gba',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='gla',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
