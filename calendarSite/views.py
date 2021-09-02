from django.shortcuts import render
from calendarSite.forms import addDataForm
from calendarSite.forms import indexForm
from calendarSite.forms import searchForm
from calendarSite.forms import subjectForm
from calendarSite.forms import userForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def addData(request):
   return render(request, 'addData.html')

def user(request):
   return render(request, 'user.html')

def subject(request):
   return render(request, 'subject.html')

