# Generated by Django 3.1 on 2020-11-14 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201114_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
    ]
