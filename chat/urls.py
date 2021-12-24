from django.urls import path
from chat import views
from .apis.index_api import getLog



urlpatterns = [
    path('', views.chat, name='chat'),
    path('getLog', getLog, name='getLog'),

]