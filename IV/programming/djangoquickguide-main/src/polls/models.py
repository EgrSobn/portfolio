from django.db import models
from django.utils import timezone

import datetime as dt

# Create your models here.

""">>> from polls.models import Choice, Question

Вывод без изменения __str__
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

Вывод с изменением __str__
>>> Question.objects.all()
<QuerySet [<Question: Is it the way?>]>"""

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self) -> bool:
        now = timezone.now()
        """Класс timedelta() модуля datetime представляет собой продолжительность, разницу между двумя датами или временем."""
        return now - dt.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text