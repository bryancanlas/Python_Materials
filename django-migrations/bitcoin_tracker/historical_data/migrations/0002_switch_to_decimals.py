# Generated by Django 2.1.5 on 2019-02-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricehistory',
            name='volume',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
