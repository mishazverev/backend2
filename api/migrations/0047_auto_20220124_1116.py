# Generated by Django 3.2.11 on 2022-01-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20220124_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalagreement',
            options={'ordering': ['additional_agreement_number']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractonetimefee',
            options={'ordering': ['one_time_fee_name']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractonetimefeesetup',
            options={'ordering': ['one_time_fee_name']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractperiodicalfee',
            options={'ordering': ['periodical_fee_name']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractperiodicalfeesetup',
            options={'ordering': ['periodical_fee_name']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractutilityfee',
            options={'ordering': ['utility_name']},
        ),
        migrations.AlterModelOptions(
            name='rentcontractutilityfeesetup',
            options={'ordering': ['utility_name']},
        ),
        migrations.AlterField(
            model_name='additionalagreement',
            name='additional_agreement_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='rentcontractonetimefee',
            name='one_time_fee_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rentcontractperiodicalfee',
            name='periodical_fee_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rentcontractsetup',
            name='building_id',
            field=models.ManyToManyField(to='api.Building'),
        ),
        migrations.AlterField(
            model_name='rentcontractutilityfee',
            name='utility_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tenantcontractorcontacts',
            name='contact_person_name',
            field=models.CharField(max_length=100),
        ),
    ]