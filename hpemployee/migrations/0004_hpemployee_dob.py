# Generated by Django 2.0.5 on 2018-05-18 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpemployee', '0003_hpemployee_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpemployee',
            name='DOB',
            field=models.DateTimeField(default=datetime.datetime(1963, 12, 2, 15, 30, 59, 354343)),
        ),
    ]
