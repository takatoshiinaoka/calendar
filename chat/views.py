from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from calendarSite.forms import addDataForm
from calendarSite.forms import SubjectForm
from calendarSite.forms import taskForm
from calendarSite.forms import TaskForm
from calendarSite.models import Calendar, User
from calendarSite.models import Task
from calendarSite.models import User_Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject
from chat.models import Log
from chat.models import Comment
from calendarSite.forms import subject_manageForm
# Create your views here.
def chat(request):
   if 'message' in request.GET:
      message = request.GET['message']
      subject_id = Subject.objects.get(id = request.GET['subject'])
      author = request.user
      comment = Comment(message = message,subject_id = subject_id,author = author)
      comment.save()
      return JsonResponse({"test":0})
   mysubjects = User_Subject.objects.filter(user_id=str(request.user.id)).all()#今ログインしているユーザーの履修情報を取得
   subjects =[]#ログイン中のユーザーが履修している科目データをすべてリストに格納
   for i in mysubjects:
      subjects.append(Subject.objects.get(id=i.subject_id))
   subject_id='0'
   if 'subject' in request.GET:
      subject_id = request.GET['subject']
   params = {
      'subjects':subjects,
      'subject_id':subject_id,
   }
   return render(request, 'report.html',params)

 