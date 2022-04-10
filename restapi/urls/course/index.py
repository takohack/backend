from django.urls import path, include
from restapi.views.course.course import getcourses


urlpatterns = [
    path("getcourses/", getcourses, name="get_courses"),
]