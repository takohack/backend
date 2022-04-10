from django.db import models


class Course(models.Model):
    courseName = models.CharField(default="", max_length=100, blank=True, null=True)
    courseId = models.CharField(default="", max_length=10, blank=True, null=True)
    courseImg = models.URLField(max_length=256, blank=True)
    teacherId = models.CharField(default="", max_length=10, blank=True, null=True)
    teacherName = models.CharField(default="", max_length=50, blank=True, null=True)
    courseTerm  = models.CharField(default="", max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.courseName)
    