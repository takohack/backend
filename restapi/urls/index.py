from django.urls import path, include
from restapi.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("courses/", include("restapi.urls.course.index")),
]