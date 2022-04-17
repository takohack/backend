from django.db import reset_queries
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from restapi.models.user.student import Student


def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confrim = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "用户名和密码不能为空"
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "用户名已存在",
        })
    if password != password_confrim:
        return JsonResponse({
            'result': "两个密码不一致",
        })

    user = User(username=username)
    user.set_password(password)
    user.save()
    Student.objects.create(
        user=user, photo="https://cdn.acwing.com/media/user/profile/photo/123395_lg_4a00b9592d.jpg")
    login(request, user)
    return JsonResponse({
        'result': "success",
    })
