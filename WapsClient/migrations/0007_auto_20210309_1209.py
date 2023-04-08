# Generated by Django 3.1.5 on 2021-03-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WapsClient', '0006_limitasset_gas_plus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='limitasset',
            old_name='curr_price',
            new_name='curr_price_for_qnty',
        ),
        migrations.AddField(
            model_name='limitasset',
            name='curr_price_per_token',
            field=models.FloatField(null=True),
        ),
    ]