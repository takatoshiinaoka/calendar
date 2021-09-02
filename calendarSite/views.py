from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
# from calendarSite.forms import searchForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def search(request):
   if request.POST:
      # form = searchForm(request.POST or None)
      subject = request.POST.getlist("subject") 
      print(subject)
   # メッセージ情報を取得。ない場合は空文字が入る
   
   """if  subject != '':
        # メッセージの内容をDBに登録
        CalendarModel = Calendar(subject=subject)
        CalendarModel.save()

    CalendarList = Calendar.objects.all()

    return render(request, 'search.html',{
        "CalendarList": CalendarList
    })

    dbData = {
        "id": 123,
        "name": "name",
        "form": form,
        "CalendarList" : CalendarList,
    }"""
   return render(request, 'search.html')

def addData(request):
   return render(request, 'addData.html')

def user(request):
   return render(request, 'user.html')

def subject(request):
   return render(request, 'subject.html')

