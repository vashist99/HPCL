# Generated by Django 2.0.5 on 2018-05-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpemployee', '0011_auto_20180528_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpemployee',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='hpemployee',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
