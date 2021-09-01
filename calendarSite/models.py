from django.db import models

# Create your models here.

class Calendar(models.Model):
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.CharField(max_length=30)
