from django.contrib import admin
from .models import Friend
from .models import Subject
from .models import Task

admin.site.register(Friend)
admin.site.register(Subject)
admin.site.register(Task)

# Register your models here.
