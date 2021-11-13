from django.urls import path
from calendarSite import views
from .apis.index_api import get_tasks
from .apis.index_api import get_task

urlpatterns = [
    path('get_tasks/<int:id>', get_tasks, name='get_tasks'),
    path('get_task/<int:id>', get_task, name='get_task'),

]
