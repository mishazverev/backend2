# Generated by Django 3.2.6 on 2021-08-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_premisemain_premise_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premisemain',
            name='premise_type',
            field=models.CharField(max_length=50),
        ),
    ]
