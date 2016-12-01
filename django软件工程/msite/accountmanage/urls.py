from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^userlogout/',views.userlogout),
    url(r'^createuser/',views.createuesr), #用户注册
    url(r'^userlogin/',views.userlogin),   #用户登入
    url(r'^uploaditems/',views.uploaditems),         #上传xx
    url(r'^information/',views.getinf),            #浏览xx 
]
