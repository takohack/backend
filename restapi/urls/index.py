from django.urls import path, include
from restapi.views.index import index
from restapi.views.index import get_comments
from restapi.views.index import update_comments
from restapi.consumers import ChatConsumer
from restapi.consumers import DisConsumer
from django.urls import re_path

urlpatterns = [
    path("", index, name="index"),
    path("courses/", include("restapi.urls.course.index")),
    path("user/",include("restapi.urls.user.index")),
    path("getcomments/",get_comments,name="get_comments"),
    path("updatecomments",update_comments,name="update_comments")
]


websocket_urlpatterns = [
    # 前端请求websocket连接
    path('wx/', ChatConsumer.as_asgi()),
    re_path('lesson/(?P<room_name>\w+)',DisConsumer.as_asgi()),
]

