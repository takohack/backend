from django.http import JsonResponse
from restapi.models.user.student import Student


def getinfo(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录"
        })
    else:
        student = Student.objects.get(user=user)
        return JsonResponse({
            'result': "success",
            'userid': student.user.username,
            'photo': student.photo,
            'username': student.student_id,
            'lesson' : student.student_choose_lesson
        })