from django.http import JsonResponse
from restapi.models.course.course import Course
from restapi.models.courseinfo.info import Info
from restapi.models.courselesson.lesson import Lesson
from django.core import serializers


def getcourses(request):
    courses = serializers.serialize("json",Course.objects.all())
    data = {"courses": courses}
    return JsonResponse(data)

def getcoursesinfo(request):
    infos = serializers.serialize("json",Info.objects.all())
    data = {"coursesinfo": infos }
    return JsonResponse(data)

def getlessons(request):
    lessons = serializers.serialize("json",Lesson.objects.all())
    data = {"lessons": lessons}
    return JsonResponse(data)