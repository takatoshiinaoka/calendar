from django.shortcuts import render
from django.shortcuts import redirect
from calendarSite.forms import addDataForm
from calendarSite.forms import SubjectForm
from calendarSite.forms import taskForm
from calendarSite.forms import subjectForm
from calendarSite.forms import TaskForm
from calendarSite.models import Calendar
from calendarSite.models import Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject
from calendarSite.forms import subject_manageForm
#以下メール用
import pandas as pd
import datetime #日付や時間を指定するモジュール
import smtplib #メールさメールサーバーを操作してメールを送信する SMTP
import ssl #暗号化や認証の仕組み
from email.mime.text import MIMEText #メールを日本語で送信できるようにするためのモジュール
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
from email.mime.multipart import MIMEMultipart #メール本文以外に添付ファイルを送信できるようにする
from email.mime.base import MIMEBase #添付ファイルの形式を指定する
from email import encoders #添付ファイルをメールで送ることができるようにする


gmail_account = "pbl2021team1@gmail.com"
gmail_password = "fitrakugaku"
# mail_to = "s20a2005@gmail.com"
# send_name = "稲岡天駿"
today_date = datetime.date.today()

#gmailを送る関数
def gmail_send(send_name, mail_to, task, delivery_date ):

  subject = "{0}様、{1}の課題の締め切りが近づいています。".format(send_name,task)
  body = '''課題締め切りのお知らせをします。<br>
            myFITをご確認ください。<br>
            {0}の期限は{1}となります。<br><br>
            プロジェクト型演習team1メンバーより'''.format(task,delivery_date)
  msg=MIMEMultipart()

  msg['Subject'] = subject
  msg['To'] = mail_to
  msg['From'] = gmail_account
  msg_body = MIMEText(body, "html")

  msg.attach(msg_body)

  server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
  server.login(gmail_account, gmail_password)
  server.send_message(msg)
  server.close()
#   print(send_name,'様：送信完了')

#トップページ(科目を指定しない場合)
def index(request):
   #gmail_send("s20a2005", "s20a2005@bene.fit.ac.jp", "課題:メールを送る関数を定義する", "2021/12/11" )
   subject_id = '0'
   task_id = '0'
   if 'subject' in request.GET:
      subject_id = request.GET['subject']
  
   if 'task' in request.GET:
      task_id = request.GET['task']
  
   tasks = Task.objects.filter(subject_id=subject_id).all() 
   task = Task.objects.filter(id=task_id).all() 
   subjects = Subject.objects.all()
   user = request.user #現在ログインしているアカウント
   if(request.method == 'POST'):
      response = redirect('/')
      get_params = request.GET.urlencode()
      response['location'] += '?'+get_params#クエリパラメータを引き継ぎたいけどうまくいかない
   
   if 'create_subject' in request.POST:
         obj = Subject()
         subject = SubjectForm(request.POST,instance=obj)
         subject.save()
         return response
         

   initial_dict={
      'subject_id' : subject_id,
   }
   dbData={
         "tasks":tasks,
         "user":user,
         "subjects":subjects,
         'subject_id' : subject_id,
         'task_id':task_id,
         'task':task,
         'form_task' : TaskForm(initial=initial_dict),
         'form_subject': SubjectForm(),
         'subject_id_i':int(subject_id),
         'task_id_i':int(task_id),
   }
   if task_id != '0':
      obj=Task.objects.get(id=task_id)
      dbData['form_editTask']=TaskForm(instance=obj)
   return render(request, 'index.html',dbData)


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

   caleList = Task.objects.all()

   print("caleList")
   print(caleList)
   user = request.user
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

def subject_manage(request):
   
   form = subject_manageForm(request.GET or None)
   print(form)
   user = request.user.id
   print(user)
   subjectid= form.data or ''
   print("これ")
   
   # print(subjectid)
   # print('test')
   print(dict(subjectid))

   if(form != None and dict(subjectid)!={}):
      # データ更新
      sql = 'DELETE FROM calendarSite_user_subject where user_id = "{{user}}"'
      #c.execute(sql)
      # db.execute(sql) #sql文を実行
      # db.close()      #データベースを閉じる
      User_Subject.objects.filter(user_id=str(user)).delete()
      for inaoka in dict(subjectid)['chk']:
         print(inaoka)
         User_SubjectModel = User_Subject(user_id=str(user),subject_id=inaoka,week="week",period="period")
         User_SubjectModel.save()
   

   
   params={
      'title':'科目管理',
      'data': Subject.objects.all(),
   }
   return render(request, 'subject_manage.html',params)

def report(request):
   subject_id = '0'
   task_id = '0'
   if 'subject' in request.GET:
      subject_id = request.GET['subject']
  
   if 'task' in request.GET:
      task_id = request.GET['task']
  
   tasks = Task.objects.filter(subject_id=subject_id).all() 
   task = Task.objects.filter(id=task_id).all() 
   subjects = Subject.objects.all()
   print("caleList")
   user = request.user #現在ログインしているアカウント
   if(request.method == 'POST'):
      if 'create_task' in request.POST:
         obj = Task(author = request.user)
         task = TaskForm(request.POST,instance=obj)
         task.save()
         return redirect(to = 'report')
      elif 'create_subject' in request.POST:
         obj = Subject()
         subject = SubjectForm(request.POST,instance=obj)
         subject.save()
         return redirect(to = 'report')
   
   dbData={
         "tasks":tasks,
         "user":user,
         "subjects":subjects,
         'subject_id' : subject_id,
         'task_id':task_id,
         'task':task,
         'form_task' : TaskForm(),
         'form_subject': SubjectForm(),
         'subject_id_i':int(subject_id),
         'task_id_i':int(task_id),
   }
   return render(request, 'report.html',dbData)

from django.core.paginator import Paginator

#todo クラスベースビューに書き換える
#課題の一覧表示
def task(request,num=1):
   if(request.method == 'POST'):
      #課題のデータをすべて変数dataに入れる(要素はmodels.py参照)※importを忘れずに！
      data = Task.objects.filter(subject_id=4).all()
   else:
      data = Task.objects.all()
   page = Paginator(data,3)
   #表示に使いたい情報を配列(辞書)paramsに代入
   params = {
      'title':'課題一覧',
      'data': page.get_page(num),
      'form':SubjectForm(),#forms.py参照 ※これもimportしないと使えない
   }
   #フォームから入力情報が送信されたら辞書に入力情報を代入
   
      

   #第２引数でテンプレートの指定、第3引数にテンプレートで使う情報を入れる
   return render(request, 'task.html',params)

#課題の作成
def create_task(request):
   path='/task/1'
   if 'subject' in request.GET:
      subject_id = request.GET['subject']
      path='/?subject='+subject_id
   if(request.method == 'POST'):
      obj = Task(author = request.user,end=request.POST['end'])
      task = TaskForm(request.POST,instance=obj)
      task.save()
      return redirect(to = path)

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
   return redirect(to = '/')

def create_subject(request):
   if (request.method == 'POST'):
      obj = Subject()
      subject = SubjectForm(request.POST,instance=obj)
      subject.save()
      return redirect(to = '/subject')
   params = {
      'title' : '科目の作成',
      'form' : SubjectForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create_subject.html',params)

def edit_subject(request,num):
   obj = Subject.objects.get(id=num)
   if(request.method == 'POST'):
      subject = SubjectForm(request.POST,instance=obj)
      subject.save()
      return redirect(to='/subject')
   params ={
      'title':'科目の編集',
      'id':num,
      'form':SubjectForm(instance=obj),
   }
   return render(request,'edit_subject.html',params)

def delete_subject(request,num):#todo ユーザーに確認するページを追加
   subject = Subject.objects.get(id=num)
   subject.delete()
   return redirect(to = '/subject')

from django.views.generic import ListView
from django.views.generic import DetailView

class SubjectView(ListView):
   model = Subject
   template_name = "subject.html"
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["title"] = "科目一覧"
        return context

class TaskDetailView(DetailView):
   model = Task
   template_name = "taskDetail.html"