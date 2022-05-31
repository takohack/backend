from django.db import models

from django.contrib.auth.models import User



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)
    student_id = models.CharField(default="", max_length=50, blank=True, null=True)
    student_choose_lesson = models.CharField(default="", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "学生管理"   
        verbose_name_plural = verbose_name     

    def __str__(self):
        return str(self.student_id)

class Sign(models.Model):
    user_name = models.CharField(default="", max_length=200, blank=True, null=True)
    sign_time = models.CharField(default="", max_length=200, blank=True, null=True)
    course = models.CharField(default="", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "签到管理"   
        verbose_name_plural = verbose_name 

    def __str__(self):
        return str("姓名: " + self.user_name + " 签到时间: "+ self.sign_time + " 签到课程: " + self.course)