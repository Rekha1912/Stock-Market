# Generated by Django 3.0.1 on 2020-10-10 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstock',
            name='action',
        ),
        migrations.RemoveField(
            model_name='userstock',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='userstock',
            name='value',
        ),
    ]
