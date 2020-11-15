from django.db import models


# Create your models here.
class Todo(models.Model):
    """todo app"""

    class Meta(object):
        db_table = 'todo'

    priorityList = [
        ("レベル1: 余裕", "余裕"),
        ("レベル2: まあまあ", "まあまあ"),
        ("レベル3: ぼちぼち", "ぼちぼち"),
        ("レベル4: やばい", "やばい"),
        ("レベル5: かなりやばい", "かなりやばい")
    ]

    # table追加予定
    title = models.CharField(verbose_name='todo text', max_length=200, default='Todo')
    completed = models.BooleanField(verbose_name='completed', default=False)
    progress = models.CharField(verbose_name='progress',choices=priorityList, default=1, max_length=20)
    importance = models.CharField(verbose_name='importance',choices=priorityList, default=1, max_length=20)
    motivation = models.CharField(verbose_name='motivation',choices=priorityList, default=1, max_length=20)
    # priority = models.IntegerField(verbose_name='priority', default=0)

    # template内で{{ todo }}と記載した際にtodo.titleが表示される
    def __str__(self):
        return self.title
