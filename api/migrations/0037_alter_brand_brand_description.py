# Generated by Django 3.2.6 on 2022-01-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20220107_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
