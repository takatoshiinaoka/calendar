from django.urls import path
from calendarSite import views
from .apis.index_api import get_tasks
from .apis.index_api import delete_task

urlpatterns = [
    path('get_tasks', get_tasks, name='get_tasks'),
    path('delete_task', delete_task, name='delete_task'),
]
