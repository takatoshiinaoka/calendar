from django.http import JsonResponse
from calendarSite.models import Task
from calendarSite.models import Subject
from calendarSite.models import User_Subject
from calendarSite.models import User_Task
from calendarSite.models import Log
from calendarSite.models import Comment

from calendarSite.forms import TaskForm


def get_tasks(request):
    subject_id = '0'
    task_id = '0'
    if 'subject' in request.GET:
      subject_id = request.GET['subject']

    if 'task' in request.GET:
      task_id = request.GET['task']
    yet=User_Task.objects.filter(user_id=str(request.user.id),task_id=Task.objects.get(id=int(task_id))).exists()
    done=""
    if not(yet):
        done="checked='checked'"
    response_data = {
        "subject_id": subject_id,
        "subject": '',
        "task_id":task_id,
        "tasks": [],
        "task":'0',
        "done":done,
    }

    if(subject_id!='0'):
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

    return {"id":data.id,"subject": data.subject_id.name, "task": data.name}

def to_detail_dict(data):
    obj = Task.objects.get(id=data.id)
    return {
        "subject": data.subject_id.name,
        "name": data.name,
        "contents":data.contents,
        "author":data.author,
        # "created_at":data.created_at,
        # "updated_at":data.updated_at,
        "end":data.end,
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
    if 'end' in request.GET:
        end = request.GET['end']
    

    subject=Subject.objects.get(id=subject_id)
    
    if 'task' in request.GET:
        id = request.GET['task']
        task = Task.objects.get(id=id)
        obj = Task(id=id,subject_id=subject,name=name,author = task.author,end=end)#todo
        #print("課題の編集を行います")
    else:
        obj = Task(subject_id=subject,name=name,author = request.user,end=end)
        #print("課題の作成を行います")
    obj.save()
    return redirect(to="/")

def save_User_Subject(request):
    subjects = Subject.objects.all()
    for i in subjects:
      if 'answer'+str(i.id) in request.GET:
        answer = request.GET['answer'+str(i.id)]
        if answer=="true":
            if not(User_Subject.objects.filter(user_id=request.user,subject_id=i).exists()):
                obj=User_Subject(user_id=request.user,subject_id=i)
                obj.save()
        elif User_Subject.objects.filter(user_id=request.user,subject_id=i).exists():
            obj=User_Subject.objects.filter(user_id=request.user,subject_id=i)
            obj.delete()
    
    return JsonResponse({'test':0})

def test(request):
    response_data = {
        "logs":[],
        "comments":[],
    }
    if 'subject' in request.GET:
        subject_id=request.GET['subject']
        objs = Log.objects.filter(subject_id=subject_id).all()
        for obj in objs:
            response_data["logs"].append(log_to_dict(obj))
        comments = Comment.objects.filter(subject_id=subject_id).all()
        if 'delete' in request.GET:
            for i in comments:
                i.delete()
        for i in comments:
            response_data["comments"].append(comments_to_dict(i))
    return JsonResponse(response_data)

def log_to_dict(data):
  
    return {"id":data.id,"user":data.user_id,"subject": data.subject_id.name,"task":data.task_id.name,"action":data.action,"created_at":data.created_at}

def comments_to_dict(data):
  
    return {"id":data.id,"author":data.author,"subject": data.subject_id.name,"message":data.message,"created_at":data.created_at}