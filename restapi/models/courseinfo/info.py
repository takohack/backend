from django.db import models


class Info(models.Model):
    courseName = models.CharField(default="", max_length=100, blank=True, null=True)
    courseId = models.CharField(default="", max_length=10, blank=True, null=True)
    coursechapters = models.CharField(default="", max_length=200, blank=True, null=True)
    coursehomework = models.CharField(default="", max_length=200, blank=True, null=True)
    coursenotice = models.CharField(default="", max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = "课程信息管理"   
        verbose_name_plural = verbose_name 
    def __str__(self):
        return str(self.courseName)