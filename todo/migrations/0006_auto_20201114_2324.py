# Generated by Django 3.1 on 2020-11-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201114_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(1, '余裕'), (2, 'まあまあ'), (3, 'ぼちぼち'), (4, 'やばい'), (5, 'かなりやばい')]),
        ),
    ]