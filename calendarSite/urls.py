from django.urls import path
from calendarSite import views
from .apis.index_api import get_tasks
from .apis.index_api import delete_task
from .apis.index_api import save_task
from .apis.index_api import test
from .apis.index_api import save_User_Subject


urlpatterns = [
    path('get_tasks', get_tasks, name='get_tasks'),
    path('delete_task', delete_task, name='delete_task'),
    path('save_task', save_task, name='save_task'),
    path('save_User_Subject', save_User_Subject, name='save_User_Subject'),
    path('test', test, name='test'),
]