from django.urls import path, include
from restapi.views.course.course import getcourses
from restapi.views.course.course import getcoursesinfo
from restapi.views.course.course import getlessons


urlpatterns = [
    path("getcourses/", getcourses, name="get_courses"),
    path("getcoursesinfo/",getcoursesinfo,name = "get_infos"),
    path("getlessons",getlessons,name= "get_lessons")
]