# Generated by Django 3.0.1 on 2020-10-11 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_userstock_latest_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstock',
            old_name='latest_price',
            new_name='lastprice',
        ),
    ]
