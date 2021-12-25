from django.urls import path
from chat import views
from .apis.index_api import getLog
from .apis.index_api import getQuestion
from .apis.index_api import getAnswer


urlpatterns = [
    path('', views.chat, name='chat'),
    path('getLog', getLog, name='getLog'),
    path('getQuestion', getQuestion, name='getQuestion'),
    path('getAnswer', getAnswer, name='getAnswer'),

    path('comments', views.comments, name='comments'),
    path('create_question', views.create_question, name='create_question'),
    path('create_answer', views.create_answer, name='create_answer'),

]