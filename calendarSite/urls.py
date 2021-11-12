from django.urls import path
from calendarSite import views
from .apis.index_api import get_name

urlpatterns = [
    path('get_name/<int:id>', get_name, name='get_name'),
    path('a',views.index,name='inde'),
]
