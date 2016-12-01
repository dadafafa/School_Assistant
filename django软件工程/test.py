import urllib.parse
import urllib.request
#界面代号：1=  登陆前界面 2=登陆后界面 3=上传界面 4=信息界面 0=退出
print("Please input server ip")
ipurl=input()
statusNo=1
mainaccount=""

def createusertest():
    print("Please input your account")
    account=input()
    print("Please input your password")
    password=input()
    values = {  
        'account': account,  
        'password': password  
    }  
    data = urllib.parse.urlencode(values)  
    data = data.encode('utf-8')  
    req = urllib.request.Request("http://%s/main/createuser/"%(ipurl), data)
    response = urllib.request.urlopen(req)
    html=response.read()
    return(html.decode('utf-8'))

def logintest():
    account=mainaccount
    print("Please input your password")
    password=input()    
    values = {  
        'account': account,  
        'password': password  
    }
    data = urllib.parse.urlencode(values)  
    data = data.encode('utf-8')  
    req = urllib.request.Request("http://%s/main/userlogin/"%(ipurl), data)
    response = urllib.request.urlopen(req)
    html=response.read()
    return(html.decode('utf-8'))

def logouttest():
    account=mainaccount
    values={
        'account':account
    }
    data = urllib.parse.urlencode(values)  
    data = data.encode('utf-8')  
    req = urllib.request.Request("http://%s/main/userlogout/"%(ipurl), data)
    response = urllib.request.urlopen(req)
    html=response.read()
    return(html.decode('utf-8'))
    
def uploadtest():
    account=mainaccount
    print("Input the item's catagory(0-9)")
    catagory=input()
    print("Input the item's shortcuts")
    shortcuts=input()
    print("Input the item's description")
    description=input()
    values={
        'account':account,
        'catagory':catagory,
        'shortcuts':shortcuts,
        'description':description
    }
    data = urllib.parse.urlencode(values)  
    data = data.encode('utf-8')  
    req = urllib.request.Request("http://%s/main/uploaditems/"%(ipurl), data)
    response = urllib.request.urlopen(req)
    html=response.read()
    return(html.decode('utf-8'))
    
    
def informationtest():
    data = urllib.parse.urlencode({})   
    url = "http://%s/main/information/"%(ipurl)
    req=urllib.request.urlopen(url)
    html=req.read()
    print(html.decode('utf-8'))

#createusertest()
#logintest()
#logouttest()
#uploadtest()
#informiontest()

while (statusNo!=0):
    if statusNo==1:
        print("************************************************")
        print("You are not logged in")
        print("Please input 1->register 2->login -1->exit")
        command=input()
        if command=="-1":
            statusNo=0
        if command=="1":
            print("************************************************")            
            ans=createusertest()
            print("************************************************")
            if ans=="1":
                print("Register succeeded")
            if ans=="2":
                print("Duplicate account")
            if ans=="-1":
                print("Error")
        if command=="2":
            print("************************************************")
            print("Please input your account")
            mainaccount=input()
            ans=logintest()
            print("************************************************")
            if ans=="1":
                print("Login succeeded")
                statusNo=2
            if ans=="2":
                print("Account does not exist")
            if ans=="3":
                print("Wrong password")
            if ans=="4":
                print("This account has already logged in")
            if ans=="-1":
                print("Error")
    if statusNo==2:
        print("************************************************")
        print("You've logged in")
        print("Please input 1->upload 2->getinformation -1->logout")
        command=input()
        if command=="-1":
            ans=logouttest()
            if ans=="1":
                print("************************************************")
                print("Logout succeeded")
                statusNo=1
            if ans=="-1":
                print("Error")
        if command=="1":
            print("************************************************")
            ans=uploadtest()
            if ans=="1":
                print("Upload succeeded")
            if ans=="-1":
                print("Error")
        if command=="2":
            print("************************************************")
            informationtest()
            print("************************************************")
                    
            
