# Generated by Django 3.0.1 on 2020-10-11 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_userstock_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstock',
            name='latest_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]