# Generated by Django 3.0.1 on 2020-10-11 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0015_auto_20201011_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Userstock'),
        ),
    ]
