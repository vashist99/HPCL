# Generated by Django 2.0.5 on 2018-05-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hpemployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('location', models.TextField()),
            ],
        ),
    ]
