# Generated by Django 3.2.6 on 2021-08-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210817_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantcontractor',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='bik',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='brands',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_mobile1',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_mobile2',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_phone',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='contact_person_position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='correspondent_account',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='current_account',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='kpp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='legal_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='legal_entity_certificate_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='legal_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_ceiling_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_cooling_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_electric_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_facade_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_max_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='needed_min_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='ogrn',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='okpo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='postal_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='registration_authority',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='retail_premise_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='signing_person_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='signing_person_position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantcontractor',
            name='tax_id',
            field=models.BigIntegerField(blank=True, default=0, null=True, unique=True),
        ),
    ]
