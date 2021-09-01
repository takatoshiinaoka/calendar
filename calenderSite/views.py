from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calender(request):
    return render(request, 'calender.html')
"""
    def serch(request):
    return render(request, 'serch.html')
"""
"""
    def addData(request):
   return render(request, 'addData.html')
"""
"""
    def user(request):
   return render(request, 'user.html')
"""
"""
    def subject(request):
   return render(request, 'subject.html')
"""

