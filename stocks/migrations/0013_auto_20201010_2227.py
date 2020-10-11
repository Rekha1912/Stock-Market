# Generated by Django 3.0.1 on 2020-10-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0012_cash'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cash',
        ),
        migrations.AddField(
            model_name='userstock',
            name='cashvalue',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
