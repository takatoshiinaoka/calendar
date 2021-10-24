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

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender =models.BooleanField()
    age = models.IntegerField(default = 0)
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + \
            self.name + '(' + str(self.age) + ')>'