# Generated by Django 2.0.5 on 2018-05-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpemployee', '0010_auto_20180528_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hpemployee',
            name='location_code',
            field=models.IntegerField(),
        ),
    ]
