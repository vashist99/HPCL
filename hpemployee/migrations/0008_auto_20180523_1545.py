# Generated by Django 2.0.5 on 2018-05-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpemployee', '0007_auto_20180523_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hpemployee',
            name='Email_id',
            field=models.EmailField(default='gnhegde@hpcl.in', max_length=100),
        ),
    ]