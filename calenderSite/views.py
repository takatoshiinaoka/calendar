from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#def serch(request):
#    return render(request, 'serch.html')