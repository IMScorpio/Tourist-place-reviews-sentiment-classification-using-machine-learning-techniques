from builtins import Exception, str
from django.shortcuts import render
from django.contrib import messages
from user.models import *
from user.forms import *
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")


def viewuserdata(request):
    s = userdata.objects.all()
    return render(request, "admin/viewuserdata.html", {"qs": s})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        userdata.objects.filter(id=uname).update(status=status)
        qs=userdata.objects.all()
        return render(request,"admin/viewuserdata.html",{"qs":qs})

def userlogincheck(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = userdata.objects.get(name=uname,passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print(status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'user/userhome.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'user/userlogin.html')

        except Exception as e:
            print('Exception is ',str(e))
            messages.success(request, 'Invalid user id and password')
        return render(request,'user/userlogin.html')

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            print("form is saved")
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})

def userlogin(request):
    return render(request,"user/userlogin.html")


def userhome(request):
    return render(request,'user/userhome.html')

def search(request):
    return render(request,'user/search.html')


def usersearchresult1(request):
    pos,neg =0,0
    semantic = 'pending'
    placename = request.GET.get('placename')
    print("placename",placename)
    qs=feedback.objects.filter(placename=placename)
    pt=[]
    nt=[]
    for x in qs:
        rtng=x.rating

        rtng=int(rtng)
        print(type(rtng))
        if rtng > 2:
            pos = pos + 1
            cmmnt = x.review
            pt.append(cmmnt)
            print(pt)
        else:
            neg=neg+1
            cmmnt=x.review
            print(nt)
            nt.append(cmmnt)

    if pos>neg:
        semantic='positive'
    elif pos<neg:
        semantic='negative'
    elif pos==neg:
        semantic='nutral'



    print("positive products:",pt)
    print("negative products:",nt)
    return render(request,"user/toursimreview.html",{"qs":qs,"sem":semantic,"pt":pt,"nt":nt})