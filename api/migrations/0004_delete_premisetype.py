# Generated by Django 3.2.6 on 2021-08-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_premisemain_premise_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PremiseType',
        ),
    ]