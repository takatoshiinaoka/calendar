from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
from calendarSite.forms import searchForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm
from calendarSite.models import Calendar

# Create your views here.
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

   # メ�?セージ�?報を取得。な�?場合�?�空�?字が入�?
   """
   if  user != '':
        # メ�?セージの�?容をDBに登録
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
   user='かい�?'
   subject='お�?��?お茶'
   title='伊藤�?'


   #フォー�?を持って来�?
   form=addDataForm(request.POST or None)
   #フォー�?から�?ータを取�?
   date=form['date'].data or ''
   user=form['user'].data or ''
   subject=form['subject'].data or ''
   title=form['title'].data or ''

   print(str(date))
   print(str(user))
   print(str(subject))
   print(str(title))

   #�?ータベ�?�スに保�?
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

