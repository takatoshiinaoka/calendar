from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
from calendarSite.forms import taskForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm
from calendarSite.models import Calendar
from calendarSite.models import Subject 

# Create your views here.


def index(request):
    return render(request, 'index.html')

def task(request):
   if request.POST:
      form = taskForm(request.POST or None)
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
   return render(request, 'task.html')

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

   print("caleList")
   print(caleList)
   user="user"
   dbData={
         "caleList":caleList,
         "user":user,
   }
   return render(request,'user.html',dbData)


def subject(request):
   form = subjectForm(request.POST or None)
   subject = form['subject'].data or ''
   print(str(subject))
   if(subject !=''):
     SubjectModel = Subject(subject=subject)
     SubjectModel.save()

   data = Subject.objects.all()
   print("data:")
   print(str(data))
   params = {
      'name' : '科目登録',
      'data' : data,
   }
   return render(request, 'subject.html',params)

def report(request):
    return render(request, 'report.html')

def memo(request):
    return render(request, 'memo.html')