from django.urls import path, include
from restapi.views.index import index
from restapi.views.index import get_comments
from restapi.views.index import update_comments

urlpatterns = [
    path("", index, name="index"),
    path("courses/", include("restapi.urls.course.index")),
    path("user/",include("restapi.urls.user.index")),
    path("getcomments/",get_comments,name="get_comments"),
    path("updatecomments",update_comments,name="update_comments")
]