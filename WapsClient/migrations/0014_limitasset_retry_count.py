# Generated by Django 3.1.5 on 2021-03-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WapsClient', '0013_wallet_bwaps_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitasset',
            name='retry_count',
            field=models.IntegerField(default=0),
        ),
    ]
