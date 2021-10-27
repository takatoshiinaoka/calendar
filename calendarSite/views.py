from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
from calendarSite.forms import searchForm
from calendarSite.forms import SubjectForm
from calendarSite.forms import userForm
from calendarSite.forms import FriendForm
from calendarSite.forms import TaskForm
from calendarSite.forms import testForm
from calendarSite.forms import searchForm
from calendarSite.models import Calendar
from calendarSite.models import Friend
from calendarSite.models import Task
from calendarSite.models import Subject
# Create your views here.


def index(request):
    return render(request, 'index.html')

def search(request):
   if request.POST:
      form = searchForm(request.POST or None)
      subject = request.POST.getlist("subject")
      user=form['user'].data or ''
      print(user)
      print(subject)

   # メッセージ情報を取得。ない場合は空文字が入る
   """
   if  user != '':
        # メッセージの内容をDBに登録
        userModel = User(user_id=user,user_subject=subject)
        userModel.save()
   
   
    UserList = User.objects.all()

    return render(request, 'search.html',{
        "UserList": UserList
    })

    dbData = {
        "id": 123,
        "name": "name",
        "form": form,
        "UserList" : UserList,
    }"""
   return render(request, 'search.html')

def addData(request):
   date=0
   user='かいた'
   subject='おーいお茶'
   title='伊藤園'


   #フォームを持って来る
   form=addDataForm(request.POST or None)
   #フォームからデータを取得
   date=form['date'].data or ''
   user=form['user'].data or ''
   subject=form['subject'].data or ''
   title=form['title'].data or ''

   print(str(date))
   print(str(user))
   print(str(subject))
   print(str(title))

   #データベースに保存
   if date!=''and user!='' and subject!='' and title!='':
      calendarModel=Calendar(date=date, user=user, title=title, subject=subject)
      calendarModel.save()

   caleList = Calendar.objects.all()

   print(caleList)

   dbData={
         "caleList":caleList,
         "date":date,
         "title":title
   }
   if date!=''and user!='' and subject!='' and title!='':
      return render(request,'user.html',dbData)
   return render(request, 'addData.html',dbData)

def user(request):
   caleList = Calendar.objects.all()

   print(caleList)
   user="user"
   dbData={
         "caleList":caleList,
         "user":user,
   }
   return render(request,'user.html',dbData)


def subject(request):
   return render(request, 'subject.html')

def report(request):
    return render(request, 'report.html')

def memo(request):
    return render(request, 'memo.html')

def chat(request):
   data = Task.objects.all()
   params = {
      'title':'課題リスト',
      'data': data,
      'form':SubjectForm(),
      'find':'',
   }
   if(request.method == 'POST'):
      params['find']=request.POST['name']

   return render(request, 'chat.html',params)

def create(request):
   if(request.method == 'POST'):
      obj = Task()
      task = TaskForm(request.POST,instance=obj)
      task.save()
      return redirect(to = '/chat')
   params = {
      'title' : 'Hello',
      'form' : TaskForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create.html',params)

def edit(request,num):
   obj = Task.objects.get(id=num)
   if(request.method == 'POST'):
      task = TaskForm(request.POST,instance=obj)
      task.save()
      return redirect(to='/chat')
   params ={
      'title':'Hello',
      'id':num,
      'form':TaskForm(instance=obj),
   }
   return render(request,'edit.html',params)

def category(request):
   params={
      'title':'科目リスト',
      'data': Subject.objects.all()
   }
   return render(request,'category.html',params)

def create_category(request):
   if (request.method == 'POST'):
      obj = Subject()
      subject = SubjectForm(request.POST,instance=obj)
      subject.save()
      return redirect(to = '/category')
   params = {
      'title' : 'Hello',
      'form' : SubjectForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create_category.html',params)
