# Generated by Django 2.0.5 on 2018-06-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_merge_20180605_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='locode',
            field=models.IntegerField(null=True),
        ),
    ]