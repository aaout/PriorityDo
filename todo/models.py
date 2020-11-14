from django.db import models


# Create your models here.
class Todo(models.Model):
    """todo app"""

    class Meta(object):
        db_table = 'todo'

    priorityList = [
        (1, "余裕"),
        (2, "まあまあ"),
        (3, "ぼちぼち"),
        (4, "やばい"),
        (5, "かなりやばい")
    ]

    # table追加予定
    title = models.CharField(verbose_name='todo text', max_length=200, default='Todo')
    completed = models.BooleanField(verbose_name='completed', default=False)
    progress = models.IntegerField(choices=priorityList, default=1)
    importance = models.IntegerField(choices=priorityList, default=1)
    motivation = models.IntegerField(choices=priorityList, default=1)
    # sum = progress + importance + motivation
    # is_validでエラーでる
    # created = models.DateTimeField(auto_created=True)

    # template内で{{ todo }}と記載した際にtodo.titleが表示される
    def __str__(self):
        return self.title
