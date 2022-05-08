from cmath import log
from django.urls import path, include
from restapi.views.user.getinfo import getinfo
from restapi.views.user.login import signin
from restapi.views.user.logout import signout
from restapi.views.user.register import register
from restapi.views.user.course import addcourse, delcourse


urlpatterns = [
    path("getinfo/",getinfo,name= "getinfo"),
    path("login",signin,name = "login"),
    path("logout",signout,name="logout"),
    path("register",register,name="register"),
    path("addcourse",addcourse,name="addcourse"),
    path("delcourse",delcourse,name="delcourse")
]
