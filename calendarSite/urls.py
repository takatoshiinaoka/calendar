from django.urls import path
from calendarSite import views
from .apis.index_api import get_tasks

urlpatterns = [
    path('get_tasks', get_tasks, name='get_tasks'),

]
