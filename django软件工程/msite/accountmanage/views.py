from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import userclass, itemclass
from django.views.decorators.csrf import csrf_exempt
import datetime
# 代码随便写的，完全不具备可编译性，只需保留def行和注释即可
#返回值 1=成功 2=重复account -1=迷之失败
@csrf_exempt
def createuesr(request):
    if request.method=='POST':
        accountstr=request.POST['account']
        passwordstr=request.POST['password']
        entry=userclass.objects.filter(account=accountstr)
        if not(entry.exists()):
            obj=userclass(account=accountstr,password=passwordstr,level=0)
            obj.save();
            return HttpResponse(1)
        else:
            return HttpResponse(2)
    return HttpResponse(-1)
    

#返回值 1=成功 2=用户名不存在 3=密码错误 4=已登陆的账号 -1=迷之失败
@csrf_exempt
def userlogin(request):
    if request.method=='POST':
        accountstr=request.POST['account']
        passwordstr=request.POST['password']
        entry=userclass.objects.filter(account=accountstr)
        if entry.exists():
            obj=entry[0]
            if obj.password==passwordstr:
                if obj.login_status==False:
                    obj.login_status=True
                    obj.save()
                    return HttpResponse(1)
                else:
                    return HttpResponse(4)
            else:
                return HttpResponse(3)
        return HttpResponse(2)    
    return HttpResponse(-1)

#返回值 1=成功 -1=迷之失败
@csrf_exempt
def uploaditems(request):
    if request.method=='POST':
        accountstr=request.POST['account']
        itemdescriptions=request.POST['description']
        itemshortcuts=request.POST['shortcuts']
        itemcatagory=request.POST['catagory']
        obj=itemclass(publisher=accountstr,descriptions=itemdescriptions,shortcuts=itemshortcuts,catagory=itemcatagory)
        obj.counter=itemclass.objects.count()
        obj.save()
        return HttpResponse(1)
    return HttpResponse(-1)

@csrf_exempt
#返回值 1=成功 -1=迷之失败
def userlogout(request):
    if request.method=='POST':     
        accountstr=request.POST['account']
        entry=userclass.objects.filter(account=accountstr)
        if entry.exists():
            obj=entry[0]
            if obj.login_status==True:
                obj.login_status=False
                obj.save()
                return HttpResponse(1)
        return HttpResponse(-1)
    return HttpResponse(-1)

#返回值应有 xx的数量 以及每个xx的具体信息 情感上这一个函数（方法）比较难写
@csrf_exempt
def getinf(request):
    if request.method=='GET':
        response=HttpResponse()
        if (itemclass.objects.count()<11):
            response.write("%d\n" % (itemclass.objects.count()))
            for obj in itemclass.objects.order_by('-counter'):
                response.write("%s\n" % (obj.shortcuts))
        else:
            response.write("10\n")
            for obj in itemclass.objects.order_by('-counter')[:10]:
                response.write("%s\n" % (obj.shortcuts))
        return response       
    else:
        return HttpResponse(-1)
    
