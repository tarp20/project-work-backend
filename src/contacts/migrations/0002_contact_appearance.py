# Generated by Django 3.2.12 on 2022-07-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='appearance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
