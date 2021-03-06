from django.db.models.query import Q
from django.db.models.sql.query import Query
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
from calendarSite.forms import subject_manageForm
from chat.models import ReactionAnswer
import datetime


def getLog(request):
    response_data = {
        "logs":[],
        "comments":[],
    }
    if 'subject' in request.GET:
        subject_id=request.GET['subject']
        objs = Log.objects.filter(subject_id=subject_id).all()
        for obj in objs:
            response_data["logs"].append(log_to_dict(obj))
        comments = Comment.objects.filter(subject_id=subject_id).all()
        if 'delete' in request.GET:
            for i in comments:
                i.delete()
        for i in comments:
            response_data["comments"].append(comments_to_dict(i))
    return JsonResponse(response_data)

def getQuestion(request):
    response_data = {
        "questions":[],
        "myquestions":[],
    }
    # return JsonResponse({"a":request.GET.getlist('subject')}) #実験コード
    conditionSubject = Q()
    filterListSubjects = request.GET.getlist('subject')
    for i in filterListSubjects:
        conditionSubject = conditionSubject | Q(subject_id=i)
    
    if 'user' in request.GET and request.GET['user']!="0":
        questions = Question.objects.filter(conditionSubject,author=request.GET['user']).all().order_by('-pk')
    else:
        questions = Question.objects.select_related().filter(conditionSubject).all().order_by('-pk')

    for q in questions:
        response_data["questions"].append(question_to_dict(q))
    
    if 'delete' in request.GET:
        for q in questions:
            q.delete()
    myquestions = Question.objects.filter(author=str(request.user))
    for i in myquestions:
        if i.resolved == False:
            response_data["myquestions"].append(i.id)
    list = response_data['questions']
    # 回答数でソート
    if 'sort' in request.GET:
        if request.GET['sort']=='comment':
            response_data['questions']=sorted(list,key=lambda x:x['answerNum'],reverse=True)
    return JsonResponse(response_data)

def getTimeToStr(time):
    dt = datetime.datetime.now()
    dt1 = datetime.datetime(year=dt.year, month=dt.month, day=dt.day, hour=0)
    dt2 = datetime.datetime(year=time.year, month=time.month, day=time.day, hour=0)
    day_diff=dt1-dt2
    if day_diff.days == 1:
        return "昨日 "+str(time.hour)+":"+str(time.minute)
    elif day_diff.days == 0:
        return "今日 "+str(time.hour)+":"+str(time.minute)
    else:
        return str(time.year) + "/" +str(time.month) + "/" + str(time.day)

def log_to_dict(data):
    num = User_Subject.objects.filter(subject_id=str(data.subject_id.id)).count()
    yet_num = User_Task.objects.filter(task_id=data.task_id).count()
    return {"id":data.id,"user":data.user_id,"subject": data.subject_id.name,
    "task":data.task_id.name,"action":data.action,"created_at":getTimeToStr(data.created_at),
    "done_num":num-yet_num,"num":num
    }

def comments_to_dict(data):
    
    return {"id":data.id,"author":data.author,
    "subject": data.subject_id.name,
    "message":data.message,
    "created_at":getTimeToStr(data.created_at)}

def question_to_dict(data):
    answerNum = Answer.objects.filter(question_id=data.id).all().count()
    return {"id":data.id,"author":data.author,"subject": data.subject_id.name,"message":data.message,
    "created_at":getTimeToStr(data.created_at),"resolved":data.resolved,"answerNum":answerNum}

def getAnswer(request):
    response_data = {
        "answers":[],
        'done':[]
    }
    if 'question' in request.GET:
        question_id=request.GET['question']
        answers = Answer.objects.filter(question_id=question_id).all()
        for a in answers:
            response_data["answers"].append(answer_to_dict(a))
    objs = ReactionAnswer.objects.filter(user_id= str(request.user.id)).all()
    for i in objs:
      response_data["done"].append(i.answer_id.id)

    return JsonResponse(response_data)

def answer_to_dict(data):
  
    return {"id":data.id,"author":data.author,"message":data.message,"created_at":getTimeToStr(data.created_at),"good_count":data.good_count}