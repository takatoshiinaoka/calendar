from django.db import models

# Create your models here.

class Calendar(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.CharField(max_length=30)

class User(models.Model):
    user_id=models.CharField(max_length=200)
    user_subject=models.CharField(max_length=200)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):#表示を決める部分
        return self.name

from django.utils import timezone

class Task(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)#科目テーブルと紐づけ
    name = models.CharField(max_length=100)
    author = models.CharField(default = '',max_length=100)
    contents = models.CharField(default='',max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新日')
    



