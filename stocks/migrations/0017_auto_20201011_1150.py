# Generated by Django 3.0.1 on 2020-10-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0016_auto_20201011_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]