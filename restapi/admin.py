from django.contrib import admin
from restapi.models.course.course import Course
from restapi.models.courseinfo.info import Info
from restapi.models.courselesson.lesson import Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(Info)
admin.site.register(Lesson)