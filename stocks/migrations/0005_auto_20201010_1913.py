# Generated by Django 3.0.1 on 2020-10-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20201010_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstock',
            name='action',
            field=models.CharField(max_length=10),
        ),
    ]
