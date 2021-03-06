# Generated by Django 3.2.9 on 2021-12-06 03:34

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0003_alter_coffee_origin_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffee',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='grinding',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 6, 3, 34, 10, 947202, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grinding',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
