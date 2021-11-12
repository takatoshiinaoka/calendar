from django.http import JsonResponse
from calendarSite.models import Subject
from calendarSite.models import Task


def get_tasks(request,id):
    response_data = {
        "message": id,
        "writers": [],
    }
    obj = Subject.objects.get(id=id)
    
    response_data["writers"].append(to_dict(obj))

    return JsonResponse(response_data)


def to_dict(data):
    return {"subject": data.id, "task": data.name}