# Generated by Django 2.2.3 on 2019-08-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Indrenievents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addnewevent',
            name='Picture',
        ),
        migrations.RemoveField(
            model_name='addnewevent',
            name='geda',
        ),
    ]
