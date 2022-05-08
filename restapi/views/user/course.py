from django.http import JsonResponse
from restapi.models.user.student import Student

def addcourse(request):
    data = request.GET
    course_id = data.get('course_id')
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录"
        })
    else:
        student = Student.objects.get(user=user)
        choose_lesson = student.student_choose_lesson
        print(choose_lesson)
        lesson_arr = choose_lesson.split(",")
        print(lesson_arr)
        if course_id in lesson_arr:
            return JsonResponse({
            'result': "已经订阅了"
        })
        else:
            lesson_arr.append(course_id)
            choose_lesson = ",".join(lesson_arr)
            student.student_choose_lesson = choose_lesson
            student.save()
        return JsonResponse({
            'result': "success"
        })


def delcourse(request):
    data = request.GET
    course_id = data.get('course_id')
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录"
        })
    else:
        student = Student.objects.get(user=user)
        choose_lesson = student.student_choose_lesson
        print(choose_lesson)
        lesson_arr = choose_lesson.split(",")
        print(lesson_arr)
        if course_id in lesson_arr:
            lesson_arr.remove(course_id)
            print(lesson_arr)
            choose_lesson = ",".join(lesson_arr)
            student.student_choose_lesson = choose_lesson
            student.save()
            return JsonResponse({
            'result': "success"
        })
        else:
            return JsonResponse({
            'result': "本来就没订阅"
            })
