from django.db import models

# Create your models here.
from calendarSite.models import Calendar, User
from calendarSite.models import Task
from calendarSite.models import User_Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject

class Log(models.Model):
    user_id = models.CharField(max_length=200)#非ログイン時に対応するため紐付けない
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')
    #action:done,create,edit,delete,cansel,
    #created_at
    #
    #good_count
    #[user]が[subject]の[task]を[action]しました。

class Comment(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    author = models.CharField(default = '',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')

class Question(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    author = models.CharField(default = '',max_length=100)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')

class Answer(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    author = models.CharField(default = '',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')
    good_count = models.IntegerField(default=0)

class ReactionAnswer(models.Model):
    user_id = models.CharField(default = '',max_length=100)
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE)
    #reaction
