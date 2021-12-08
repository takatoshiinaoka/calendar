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
from calendarSite.forms import subject_manageForm



# Create your views here.


def index(request):#トップページ(科目を指定しない場合)
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
      response = redirect('/')
      get_params = request.GET.urlencode()
      response['location'] += '?'+get_params#クエリパラメータを引き継ぎたいけどうまくいかない
   
   if 'create_subject' in request.POST:
         obj = Subject()
         subject = SubjectForm(request.POST,instance=obj)
         subject.save()
         return response
         
   print(tasks)
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
   form = subject_manageForm(request.POST or None)
   return render(request, 'subject_manage.html')

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