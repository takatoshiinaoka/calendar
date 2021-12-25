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
from chat.models import Question
from chat.models import Answer
from chat.models import ReactionAnswer
from calendarSite.forms import subject_manageForm
# Create your views here.
def chat(request):
  
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

def comments(request):
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
   return render(request, 'comments.html',params)

def create_question(request):
   if 'message' in request.GET:
      message = request.GET['message']
      subject_id = Subject.objects.get(id = request.GET['subject'])
      author = request.user
      Question(message = message,subject_id = subject_id,author = author,resolved=False).save()
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
   return render(request, 'create_question.html',params)

def create_answer(request):
   if 'message' in request.GET:
      message = request.GET['message']
      author = request.user
      Answer(message = message,question_id = Question.objects.get(id=request.GET['question']),author = author,good_count=0).save()
      return JsonResponse({"test":0})
   if 'good' in request.GET:
      user = request.user.id
      answer = Answer.objects.get(id=request.GET['good'])
      good_count = answer.good_count
      
      if ReactionAnswer.objects.filter(user_id= str(request.user.id),answer_id=answer.id).all().count() == 0:
         Answer(id=answer.id,author=answer.author,
         question_id=answer.question_id,created_at=answer.created_at,
         message=answer.message,good_count=good_count+1).save()
      ReactionAnswer(user_id=str(request.user.id),answer_id=answer).save()
      
   if 'question' in request.GET:
      question = Question.objects.get(id=request.GET['question'])
   params = {
      'question':question,
   }
   return render(request, 'create_answer.html',params)