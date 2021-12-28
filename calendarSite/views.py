from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from calendarSite.forms import addDataForm
from calendarSite.forms import SubjectForm
from calendarSite.forms import taskForm
from calendarSite.forms import TaskForm
from calendarSite.models import Calendar
from calendarSite.models import Task
from calendarSite.models import User_Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject
from calendarSite.forms import subject_manageForm
from chat.models import Log
from chat.models import Comment
#以下メール用
#import pandas as pd
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
   #print("hello")
   #gmail_send("s20a2005", "s20a2005@bene.fit.ac.jp", "課題:メールを送る関数を定義する", "2021/12/11" )
   subject_id = '0'
   task_id = 0
   if 'subject' in request.GET:
      if request.GET['subject'] != 'undefined':
         subject_id = request.GET['subject']
  
   if 'task' in request.GET:
      task_id = int(request.GET['task'])
  


   task = Task.objects.filter(id=task_id).all() 

   mysubjects = User_Subject.objects.filter(user_id=str(request.user.id)).all()#今ログインしているユーザーの履修情報を取得
   subjects =[]#ログイン中のユーザーが履修している科目データをすべてリストに格納
   for i in mysubjects:
      subjects.append(Subject.objects.get(id=i.subject_id))

   if subject_id == '0':
      tasks = []
      for i in subjects:
         tasks.extend(Task.objects.filter(subject_id=i.id).all())
          
   else:
      tasks = Task.objects.filter(subject_id=subject_id).all()

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


   if 'edit_task' in request.GET:
  
      task_id = int(request.GET["edit_task"])
      if 'task_id' in request.GET:
         if User_Task.objects.filter(user_id=str(request.user.id),task_id = Task.objects.get(id=task_id)).count() != 0:
            obj = User_Task.objects.get(user_id=str(request.user.id),task_id = Task.objects.get(id=task_id))
            obj.delete()
      else:
         num = User_Task.objects.filter(user_id=str(request.user.id),task_id = Task.objects.get(id=task_id)).count()
         if num == 0:
            user_task = User_Task(
               user_id= str(request.user.id),
               task_id = Task.objects.get(id=task_id),
               done = "true",
               notice = "",
               howlong = "",
            )
            user_task.save()
      task = Task.objects.get(id=request.GET['edit_task'])
      contents=''
      if 'contents' in request.GET:
         contents = request.GET['contents']
      obj = Task(
         id = task_id,
         subject_id=task.subject_id,
         name = request.GET['name'],
         author = task.author,
         contents = contents,
         end = task.end,
      )
      obj.save()
      return redirect('/?subject='+str(task.subject_id.id))

   yet_tasks = []
   yet = User_Task.objects.filter(user_id=str(request.user.id)).all()
   for i in yet:
      task = i.task_id
      obj = Task.objects.get(id = task.id)
      yet_tasks.append(obj.id)

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
         'form_subject': SubjectForm(),
         'subject_id_i':int(subject_id),
         'task_id_i':int(task_id),
         'yet_tasks':yet_tasks,
   }
   
#   print(str(subjects))
   if task_id != 0:
      obj=Task.objects.get(id=str(task_id))
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
   user=''
   subject=''
   title=''
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

def subject_manage(request):
   
   form = subject_manageForm(request.GET or None)

   #print(form)
   user = request.user.id
   #print(user)
   subjectid= form.data or ''

   #print("これ")
   
   # print(subjectid)
   # print('test')
   #print(dict(subjectid))
   user = request.user.id
   subjectid= form.data or ''

   if(form != None and dict(subjectid)!={}):
      #sql = 'DELETE FROM calendarSite_user_subject where user_id = "{{user}}"'
      #c.execute(sql)
      # db.execute(sql) #sql文を実行
      # db.close()      #データベースを閉じる
      User_Subject.objects.filter(user_id=str(user)).delete()#まずログインユーザーの履修データをすべて消す
      for inaoka in dict(subjectid)['chk']:
         #print(inaoka)
         User_SubjectModel = User_Subject(user_id=str(user),subject_id=inaoka)
         User_SubjectModel.save()
      return redirect('index')


   
   list = User_Subject.objects.filter(user_id=str(user))
   mysubjects = []#現在履修している科目は最初からチェックをつけておく
   for i in list:
      mysubjects.append(Subject.objects.get(id=i.subject_id))
       

   
   params={
      'data': Subject.objects.all(),
      'mysubjects':mysubjects,
   }
   return render(request, 'subject_manage.html',params)



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
   subject = Subject(id=request.POST['subject_id'])
   if(request.method == 'POST'):
      obj = Task(
      subject_id=subject,
      name=request.POST['name'],
      contents=request.POST['contents'],
      author = request.user,
      end=request.POST['end'],
      )
     
         
      # 登録
      obj.save()     
      RegistID = Task.objects.order_by('-pk')[:1].values()[0]['id']
      log = Log(user_id=str(request.user),subject_id=subject,task_id=Task.objects.get(id=RegistID),action="追加")
      log.save()
      users = User_Subject.objects.filter(subject_id=request.POST['subject_id'])
      for i in users:
         yet = User_Task(
            user_id = str(i.user_id),
            task_id = Task.objects.get(id=RegistID),
            done = 'true',
            notice = '',
            howlong = '',
         )
         yet.save()

      return redirect(to = path)

   params = {
      'title' : '課題の作成',
      # 'form' : TaskForm(),
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

# def edit_task2(request):
#    if(request.method == 'GET'):


def delete_task(request,num):#todo ユーザーに確認するページを追加
   User_Task.objects.filter(task_id=Task.objects.get(id=num)).delete()
   task = Task.objects.get(id=num)
   task.delete()
   return redirect(to = '/')


def create_subject(request):
   if (request.method == 'POST'):
      subject = Subject(name = request.POST['name'],week=request.POST['week'],period=request.POST['period'])
      subject.save()
      return redirect(to = '/subject')
   params = {
      'title' : '科目の作成',
      'form' : SubjectForm(),
      'data': Subject.objects.all()
   }
   return render(request,'create_subject.html',params)

def edit_subject(request,num):
   if(request.method == 'POST'):
      subject = Subject(id=num,name = request.POST['name'],week=request.POST['week'],period=request.POST['period'])
      subject.save()
      return redirect(to='/subject')
   try:
      subject = Subject.objects.get(id=num)
      subject_form = SubjectForm(initial = {
         'name': subject.name,   # 初期値
         'week': subject.week,
         'period':subject.period,
      })
    #  取得できなければ初期値を設定しない
   except:
      subject_form = SubjectForm()
   params ={
      'title':'科目の編集',
      'id':num,
      'form':subject_form,
   }
   return render(request,'edit_subject.html',params)

def delete_subject(request,num):#todo ユーザーに確認するページを追加
   User_Subject.objects.filter(subject_id=num).delete()
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
        return context

class TaskDetailView(DetailView):
   model = Task
   template_name = "taskDetail.html"