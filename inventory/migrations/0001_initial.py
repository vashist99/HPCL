# Generated by Django 2.0.5 on 2018-05-31 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.TextField(max_length=100)),
                ('item_des', models.TextField(max_length=100)),
                ('activity', models.TextField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('locode', models.IntegerField()),
            ],
        ),
    ]
