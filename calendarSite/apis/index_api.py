from django.http import JsonResponse
from calendarSite.models import Subject
from calendarSite.models import Task


def get_name(request,id):
    response_data = {
        "message": 'Hello!',
        "writers": [],
    }
    objs = Task.objects.filter(subject_id=id).all()
    
    for obj in objs:
        response_data["writers"].append(to_dict(obj))

    return JsonResponse(response_data)


def to_dict(data):
    return {"subject": data.subject_id.name, "task": data.name}