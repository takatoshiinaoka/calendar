from django.http import JsonResponse
from calendarSite.models import Subject
from calendarSite.models import Task


def get_tasks(request,id):
    response_data = {
        "message": id,
        "writers": [],
    }
    objs = Task.objects.filter(subject_id=id).all()
    for obj in objs:
        response_data["writers"].append(to_dict(obj))

    return JsonResponse(response_data)

def get_task(request,id):
    response_data = {
        "message": id,
        "datas": [],
    }
    obj = Task.objects.get(id=id)
    response_data["datas"].append(to_detail_dict(obj))

    return JsonResponse(response_data)

def to_dict(data):

    return {"id":data.id,"subject": data.subject_id.name, "task": data.name,"updated_at":data.updated_at}

def to_detail_dict(data):
  
    return {
        "id":data.id,
        "subject": data.subject_id.name,
        "task": data.name,
        "contents":data.contents,
        "author":data.author,
        "created_at":data.created_at,
        "updated_at":data.updated_at,
    }

