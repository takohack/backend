from django.http import JsonResponse
from restapi.models.user.student import Sign


def sign(request):
    data = request.GET
    username = data.get("username", "").strip()
    sign_time = data.get("time", "").strip()
    course = data.get("course","").strip()
    Sign.objects.create(user_name = username,sign_time = sign_time,course = course)
    return JsonResponse({
        'result': "success",
    })