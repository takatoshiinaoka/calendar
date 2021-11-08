from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm


from calendarSite.forms import SubjectForm

from calendarSite.forms import taskForm
from calendarSite.forms import subjectForm

from calendarSite.forms import userForm
from calendarSite.forms import FriendForm
from calendarSite.forms import TaskForm
from calendarSite.forms import testForm
from calendarSite.models import Calendar
from calendarSite.models import Friend
from calendarSite.models import Task
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

from django.core.paginator import Paginator

#課題の一覧表示
def task(request,num=1):
   #課題のデータをすべて変数dataに入れる(要素はmodels.py参照)※importを忘れずに！
   data = Task.objects.all()
   page = Paginator(data,3)
   #表示に使いたい情報を配列(辞書)paramsに代入
   params = {
      'title':'課題リスト',
      'data': page.get_page(num),
      'form':SubjectForm(),#forms.py参照 ※これもimportしないと使えない
      'find':'',
   }
   #フォームから入力情報が送信されたら辞書に入力情報を代入
   if(request.method == 'POST'):
      params['find']=request.POST['name']

   #第２引数でテンプレートの指定、第3引数にテンプレートで使う情報を入れる
   return render(request, 'task.html',params)

#課題の作成
def create_task(request):
   if(request.method == 'POST'):
      obj = Task(author = request.user)
      task = TaskForm(request.POST,instance=obj)
      task.save()
      return redirect(to = '/task/1')
   params = {
      'title' : '課題の作成',
      'form' : TaskForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create_task.html',params)

#課題の編集　どのデータを編集するかをnumでもらう
def edit_task(request,num):
   obj = Task.objects.get(id=num)
   if(request.method == 'POST'):
      task = TaskForm(request.POST,instance=obj)
      task.save()
      return redirect(to='/task/1')
   params ={
      'title':'課題の編集',
      'id':num,
      'form':TaskForm(instance=obj),
   }
   return render(request,'edit_task.html',params)

def delete_task(request,num):#todo ユーザーに確認するページを追加
   task = Task.objects.get(id=num)
   task.delete()
   return redirect(to = '/task/1')

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
      'title' : '科目の作成',
      'form' : SubjectForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create_category.html',params)

def edit_category(request,num):
   obj = Subject.objects.get(id=num)
   if(request.method == 'POST'):
      subject = SubjectForm(request.POST,instance=obj)
      subject.save()
      return redirect(to='/category')
   params ={
      'title':'科目の編集',
      'id':num,
      'form':SubjectForm(instance=obj),
   }
   return render(request,'edit_category.html',params)

def delete_category(request,num):#todo ユーザーに確認するページを追加
   category = Subject.objects.get(id=num)
   category.delete()
   return redirect(to = '/category')
