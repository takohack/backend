from django.db import models

from django.contrib.auth.models import User



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)
    student_id = models.CharField(default="", max_length=50, blank=True, null=True)
    student_choose_lesson = models.CharField(default="", max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.user)