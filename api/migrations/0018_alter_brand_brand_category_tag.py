# Generated by Django 3.2.6 on 2021-10-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_tenantcontractor_brands_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_category_tag',
            field=models.ManyToManyField(null=True, to='api.CategoryTag'),
        ),
    ]
