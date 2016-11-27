#coding=utf-8
from django.shortcuts import render,render_to_response
from django import forms
from .models import User,itemclass
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
import datetime
from django.utils import timezone


# 接收POST请求数据
class userFormlogin(forms.Form):
      username = forms.CharField(label='用户名',max_length=100)
      password = forms.CharField(label='密码',widget=forms.PasswordInput())



def login (request):                          #登录
      if request.method == "POST":
            uform = userFormlogin(request.POST)
            if uform.is_valid():
                  username = uform.cleaned_data['username']  #get 表单
                  password = uform.cleaned_data['password']

                  userResult = User.objects.filter(username=username,password=password)

                  if (len(userResult)>0):  #表示有此人
                        request.session['username'] = username
                        return HttpResponseRedirect('/myapp/index/')  #弹出登录成功页面

                  else:
                        return HttpResponse("该用户不存在")                 #登录失败
      else:
            uform = userFormlogin()

      return render(request,"myapp/userlogin.html",{'uform':uform})       


class userRegister(forms.Form):
      username = forms.CharField(label='用户名',max_length=100)
      password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
      password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
      email = forms.EmailField(label='电子邮件')


                     
def register(request):
      if (request.method !="POST"):
            uform =userRegister()
            
      else:
            uform =userRegister(request.POST)
            if uform.is_valid():
                  username =  uform.cleaned_data['username']
                  errors = []  

                  userResult =User.objects.filter(username = username)

                  if (len(userResult) ==1 ) :         #用户存在
                       errors.append("用户名已经存在")
                       return render(request,"myapp/userRegister.html",{"errors":errors})
                  else:
                        password1 = uform.cleaned_data['password1']
                        password2 = uform.cleaned_data['password2']            #得到表单

                        if (password1 !=password2):
                              errors.append("密码不一样请重新输入")
                              uform = userFormlogin()
                              return render(request,"myapp/userRegister.html",{"errors":errors }) 
                        else:                              
                              email = uform.cleaned_data['email']
                              password = password1

                              user = User.objects.create(username=username,password=password,email=email)       
                              user.save()
                              uform = userFormlogin()
                              return render_to_response("myapp/userRegister.html",{"errors":"注册成功"})

      return render_to_response("myapp/userRegister.html",{"uform":uform}) 



def index(request):
    name=request.session.get('username')
    if( str(name)== "None"):
          return HttpResponseRedirect('/myapp/login')

      
    username = request.session.get('username','nobody')
    latest_shortcuts_list = itemclass.objects.order_by('-pub_date')[:100]          #begin
        
    return render_to_response("myapp/index.html",{"username":username,"latest_shortcuts_list":latest_shortcuts_list})

def detail(request,itemclass_id):
    try:
         itemClass = itemclass.objects.get(pk=itemclass_id)
    except itemclass.DoesNotExist:
        raise Http404("itemclass does not exist")
    return render(request, 'myapp/detail.html', {'itemClass': itemClass})


def logout(request):
    try:
          
         del request.session['username']  #删除session
         return HttpResponseRedirect('/myapp/login/')
    except KeyError:
         return HttpResponseRedirect('/myapp/login/')






class userUpload(forms.Form):
      shortcuts = forms.CharField(label='标题',max_length=50)
      descriptions = forms.CharField(label="内容",widget=forms.Textarea())




def upload(request):
    name=request.session.get('username')
    if( str(name)== "None"):
          return HttpResponseRedirect('/myapp/login')
      
    if(request.session.get('username')=='nobody'):
         return HttpResponseRedirect('/myapp/login/')
    else:
        if(request.method =="POST"):
            uform = userUpload(request.POST)
            if uform.is_valid():
                  shortcuts = uform.cleaned_data['shortcuts']
                  descriptions= uform.cleaned_data['descriptions']
                  user = User.objects.get(username = request.session.get('username'))
                  #item = itemclass.objects.create(shortcuts=shortcuts)
                  item = itemclass.objects.create(shortcuts=shortcuts,descriptions=descriptions,user =user,pub_date = timezone.now() )
                  item.save()
                  return HttpResponseRedirect('/myapp/index/')
        else:
            uform = userUpload()
        return render(request,"myapp/userUpload.html",{"uform":uform})





class userPassword(forms.Form):
      password1 = forms.CharField(label='新密码',widget=forms.PasswordInput())
      password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())





def change_password(request):
      name=request.session.get('username')
      if( str(name)== "None"):
         return HttpResponseRedirect('/myapp/login')
      
      name=request.session.get('username')
    
      errors=[]
      if (request.method !="POST"):
            uform =userPassword()

      else:
            uform =userPassword(request.POST)
            if uform.is_valid():
                  password1 = uform.cleaned_data['password1']
                  password2 = uform.cleaned_data['password2']            #得到表单

                  if (password1 !=password2):
                        errors.append("密码不一样请重新输入")
                        uform = userPassword()
                        return render(request,"myapp/changePassword.html",{"uform":uform,"errors":errors }) 
                  else:                              
                        password = password1
                        user = User.objects.get(username=name)
                        user.password = password
                        user.save()
                        uform = userPassword()
                        diction = {"uform":uform, "errors":"密码更改成功"}
                        return render_to_response("myapp/changePassword.html",diction)

      return render(request,"myapp/changePassword.html",{"uform":uform,})





def delete(request):
      name=request.session.get('username')
      if( str(name)== "nobody"):
         return HttpResponseRedirect('/myapp/login')
            
      user = User.objects.get(username = name)
      item_class = itemclass.objects.filter(user =user )
      if (len(item_class)==0):
            content={
                  "item_class":item_class,
                  "tips":"对不起你还未发表任何信息（或已经删除）。",
                  }
      else:
            content={
                  "item_class":item_class,
                  }
      return render(request,"myapp/deleteView.html",content)




def delete_deal(request):
    name=request.session.get('username')
    if( str(name)== "nobody"):
         return HttpResponseRedirect('/myapp/login')
      
    name=request.session.get('username')
    user = User.objects.get(username = name)
    item_class = itemclass.objects.filter(user =user )
     #return HttpResponse("该用户不存在"
    try:
        pk=int(request.POST['shortcuts'])-1
    except (KeyError,RuntimeError):

        return render(request, 'myapp/deleteView.html', {
            'item_class': item_class,
            'error_message': "You didn't select a choice.",
        })
    else:
        if (pk <0):
              return HttpResponseRedirect('/myapp/delete')
        else:
              item_class[pk].delete()
              return HttpResponseRedirect('/myapp/delete')
      
      
      


      
      
