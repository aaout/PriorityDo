from django.db import models


# Create your models here.
class Todo(models.Model):
    """todo app"""

    class Meta(object):
        db_table = 'todo'

    priorityList = [
        ("余裕", "余裕"),
        ("まあまあ", "まあまあ"),
        ("ぼちぼち", "ぼちぼち"),
        ("やばい", "やばい"),
        ("かなりやばい", "かなりやばい")
    ]

    # table追加予定
    title = models.CharField(verbose_name='todo text', max_length=200)
    completed = models.BooleanField(verbose_name='completed', default=False)
    priority = models.CharField(max_length=10, choices=priorityList, default='ぼちぼち')
    # is_validでエラーでる
    # created = models.DateTimeField(auto_created=True)

    # template内で{{ todo }}と記載した際にtodo.titleが表示される
    def __str__(self):
        return self.title
