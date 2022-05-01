
from curses.ascii import NUL
from tokenize import Comment
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

def index(request):
    return render(request,"index.html")


def get_comments(request):
    print(cache.keys('*'))
    # cache.set("comments", "wuhu",timeout=None)
    if cache.has_key("comments"):
        comments = cache.get("comments")
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
        cache.set("comments",comments,timeout=None)
        return JsonResponse({
        'result':comments
    })