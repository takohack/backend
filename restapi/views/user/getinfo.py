from django.http import JsonResponse
from restapi.models.user.student import Student


def getinfo(request):
    user = request.user
    print(user)
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录"
        })
    else:
        student = Student.objects.get(user=user)
        return JsonResponse({
            'result': "success",
            'username': student.user.username,
            'photo': student.photo,
        })