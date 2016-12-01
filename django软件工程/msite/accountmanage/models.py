import datetime
from django.db import models
from django.utils import timezone

class userclass(models.Model):
    #level越大权限越高
    level=models.IntegerField(default=0)
    #账号
    account=models.CharField(max_length=200)
    #创建时间
    #createdate=models.DateTimeField('date published')
    #密码
    password=models.CharField(max_length=200)
    #登录状态 false=未登录 true=登录
    login_status=models.BooleanField(default=False)
    def __str__(self):
        return self.account

class itemclass(models.Model):
    #发布人
    publisher=models.CharField(max_length=200)
    #描述
    descriptions=models.TextField(max_length=12450)
    #简述
    shortcuts=models.CharField(max_length=997)
    #发布时间
    #pub_date=models.DateTimeField('date published')
    #类别（范围1-9）
    catagory=models.IntegerField(default=1)
    counter=models.IntegerField(default=0)
