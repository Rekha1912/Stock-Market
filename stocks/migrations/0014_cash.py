# Generated by Django 3.0.1 on 2020-10-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0013_auto_20201010_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashvalue', models.FloatField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Userstock')),
            ],
        ),
    ]
