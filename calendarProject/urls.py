"""calenderProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calendarSite import views
from django.urls import include, path
from calendarSite.views import SubjectView
from calendarSite.views import TaskDetailView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index,  name="index"),
    path('admin/', admin.site.urls),
    path('addData', views.addData, name="addData"),
    path('task', views.task, name="task"),
    path('user', views.user, name="user"),
    path('report', views.report, name="report"),
    path('task/<int:num>', views.task, name="task"),
    path('create_task', views.create_task, name="create_task"),
    path('edit_task/<int:num>',views.edit_task,name='edit_task'),
    path('delete_task/<int:num>',views.delete_task,name='delete_task'),
    path('subject', SubjectView.as_view()),
    path('taskDetail/<int:pk>', TaskDetailView.as_view()),
    path('create_subject', views.create_subject, name="create_subject"),
    path('edit_subject/<int:num>',views.edit_subject,name='edit_subject'),
    path('delete_subject/<int:num>', views.delete_subject, name="delete_subject"),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', TemplateView.as_view(template_name = 'login.html'), name='login'),
    path('app/', include('calendarSite.urls')),
]
