# -*- coding:utf-8 -*-
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题内容')
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='选择理由')
    votes = models.IntegerField(default=0, verbose_name='投票数')

    def __str__(self):
        return self.choice_text

