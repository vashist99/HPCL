# Generated by Django 2.0.5 on 2018-06-12 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_child_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='location',
            new_name='loc',
        ),
    ]