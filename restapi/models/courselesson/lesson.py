from django.db import models


class Lesson(models.Model):
    lessonbelong = models.CharField(default="", max_length=100, blank=True, null=True)
    lessonname = models.CharField(default="", max_length=100, blank=True, null=True)
    lessonexrcise = models.CharField(default="", max_length=400, blank=True, null=True)
    lessonreference = models.CharField(default="", max_length=400, blank=True, null=True)
    lessonhomework = models.CharField(default="", max_length=400, blank=True, null=True)
    
    class Meta:
        verbose_name = "课堂管理"   
        verbose_name_plural = verbose_name 
    def __str__(self):
        return str(self.lessonname + " 所属课程:" + self.lessonbelong)