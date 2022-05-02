
from curses.ascii import NUL
from tokenize import Comment
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

def index(request):
    return render(request,"index.html")


def get_comments(request):
    data = request.GET
    if not data:
        return JsonResponse({
        'result':"fail"
    })
    else:
        course_id = data.get('courseid')
        redis_key = "comments" + str(course_id)
        print(redis_key)
        if cache.has_key(redis_key):
            comments = cache.get(redis_key)
            return JsonResponse({
            'result':comments
            })
        else:
            return JsonResponse({
            'result':"fali"
        })  

def update_comments(request):
    data = request.GET
    if not data:
        return JsonResponse({
        'result':"fail"
    })
    else:
        comments = data.get('comments')
        course_id = data.get('courseid')
        redis_key = "comments" + str(course_id)
        cache.set(redis_key,comments,timeout=None)
        return JsonResponse({
        'result':comments
    })