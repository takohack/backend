from django.http import JsonResponse
from restapi.models.course.course import Course
from django.core import serializers


def getcourses(request):
    courses = serializers.serialize("json",Course.objects.all())
    data = {"courses": courses}
    return JsonResponse(data)