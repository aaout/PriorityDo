# Generated by Django 3.1 on 2020-11-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='importance',
            field=models.IntegerField(choices=[(1, '余裕'), (2, 'まあまあ'), (3, 'ぼちぼち'), (4, 'やばい'), (5, 'かなりやばい')], default=1, verbose_name='importance'),
        ),
        migrations.AddField(
            model_name='todo',
            name='motivation',
            field=models.IntegerField(choices=[(1, '余裕'), (2, 'まあまあ'), (3, 'ぼちぼち'), (4, 'やばい'), (5, 'かなりやばい')], default=1, verbose_name='motivation'),
        ),
        migrations.AddField(
            model_name='todo',
            name='progress',
            field=models.IntegerField(choices=[(1, '余裕'), (2, 'まあまあ'), (3, 'ぼちぼち'), (4, 'やばい'), (5, 'かなりやばい')], default=1, verbose_name='progress'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='Todo', max_length=200, verbose_name='todo text'),
        ),
    ]