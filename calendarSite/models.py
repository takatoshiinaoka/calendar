from django.db import models
from django.utils import timezone

# Create your models here.

class Calendar(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.CharField(max_length=30)

class User(models.Model):
    user_id=models.CharField(max_length=200)
    user_subject=models.CharField(max_length=200)
    twitter_id=models.CharField(max_length=200)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):#表示を決める部分
        return self.name


class Task(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)#科目テーブルと紐づけ
    name = models.CharField(max_length=100)
    author = models.CharField(default = '',max_length=100)
    contents = models.CharField(blank=True,default='',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新日')
    end = models.DateTimeField(default=timezone.now())
    
class User_Subject(models.Model):
    user_id=models.CharField(max_length=200)
    subject_id=models.CharField(max_length=200)
    week=models.CharField(max_length=200)
    period=models.CharField(max_length=200)


