# Generated by Django 3.1.5 on 2021-03-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WapsClient', '0009_asset_decimals'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='price_for_token',
            field=models.FloatField(null=True),
        ),
    ]
