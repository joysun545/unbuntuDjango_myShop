# Generated by Django 2.2.24 on 2022-06-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20220626_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='isdefault',
            field=models.IntegerField(default=False),
        ),
    ]
