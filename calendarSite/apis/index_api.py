from django.http import JsonResponse
from calendarSite.models import Task
from calendarSite.models import Subject
from calendarSite.forms import TaskForm


def get_tasks(request):
    subject_id = '0'
    task_id = '0'
    if 'subject' in request.GET:
      subject_id = request.GET['subject']

    if 'task' in request.GET:
      task_id = request.GET['task']
    
    response_data = {
        "subject_id": subject_id,
        "subject": '',
        "task_id":task_id,
        "tasks": [],
        "task":'0',
    }

    
    subject = Subject.objects.get(id=subject_id)
    response_data["subject"]=(subject_to_dict(subject))
    objs = Task.objects.filter(subject_id=subject_id).all()
    for obj in objs:
        response_data["tasks"].append(to_dict(obj))

    if task_id!= '0':
        task = Task.objects.get(id=task_id)
        response_data["task"]=(to_detail_dict(task))

    return JsonResponse(response_data)

def subject_to_dict(data):
    return {"id":data.id,"name":data.name}

def to_dict(data):

    return {"id":data.id,"subject": data.subject_id.name, "task": data.name,"updated_at":data.updated_at}

def to_detail_dict(data):
    obj = Task.objects.get(id=data.id)
    return {
        "subject": data.subject_id.name,
        "name": data.name,
        "contents":data.contents,
        "author":data.author,
        "created_at":data.created_at,
        "updated_at":data.updated_at,
        #"form":TaskForm(request.POST,instance=obj),
    }

from django.shortcuts import redirect

def delete_task(request):#todo ユーザーに確認するページを追加
    path='/'
    num='0'
    if 'subject' in request.GET:
        subject_id = request.GET['subject']
        path='/?subject='+subject_id
    if 'task' in request.GET:
        num = request.GET['task']
        task = Task.objects.get(id=num)
        task.delete()
    
    return redirect(to=path)

def save_task(request):
    
    if 'subject' in request.GET:
        subject_id = request.GET['subject']
    if 'name' in request.GET:
        name = request.GET['name']
    if 'start' in request.GET:
        start = request.GET['start']
    if 'goal' in request.GET:
        goal = request.GET['goal']
    if 'created_at' in request.GET:
        created_at = request.GET['created_at']
    
    subject=Subject.objects.get(id=subject_id)
    if 'task' in request.GET:
        id = request.GET['task']
        obj = Task(id=id,subject_id=subject,name=name,author = request.user,start=start,goal=goal,created_at=created_at)#todo
        print("課題の編集を行います")
    else:
        obj = Task(subject_id=subject,name=name,author = request.user,start=start,goal=goal)
        print("課題の作成を行います")
    obj.save()
    return redirect(to="/")