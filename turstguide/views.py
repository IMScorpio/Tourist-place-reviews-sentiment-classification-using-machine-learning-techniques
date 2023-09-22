from django.shortcuts import render
from builtins import Exception, str
from django.contrib import messages
from turstguide.models import *
from turstguide.forms import *
from django.http import HttpResponse
from user.forms import *


def viewguidedata(request):
    s = guidemodel.objects.all()
    return render(request, "admin/viewguidedata.html",{"qs":s})

def activateguide(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        guidemodel.objects.filter(id=uname).update(status=status)
        qs=guidemodel.objects.all()
        return render(request,"admin/viewguidedata.html",{"qs":qs})

def guidelogincheck(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = guidemodel.objects.get(name=uname,passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            request.session['name'] = check.name
            print("name",check.name)
            status = check.status
            print(status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'guide/guidehome.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'guide/guidelogin.html')

        except Exception as e:
            print('Exception is ',str(e))
            messages.success(request, 'Invalid user id and password')
        return render(request,'guide/guidelogin.html')

def guideregister(request):
    if request.method=='POST':
        form1=guideForm(request.POST)
        if form1.is_valid():
            print("form is saved")
            form1.save()
            return render(request, "guide/guidelogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=guideForm()
        return render(request,"guide/guideregister.html",{"form":form})

def guidelogin(request):
    return render(request,"guide/guidelogin.html")


def guidehome(request):
    return render(request,'guide/guidehome.html')


def uploaddata(request):
    if request.method == 'POST':
        form = uploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("save data")
            return render(request,'guide/uploaddata.html')
        else:
            print("form not valied")
    else:
        form=uploadForm()
    return render(request,'guide/uploaddata.html',{'form':form})


def touristplaces(request):
    s=upload.objects.all()
    return render(request,'guide/touristplaces.html',{"obj":s})


def viewplaces(request):
    if request.method == 'POST':
        print("hello")
        form=feedbackform(request.POST)
        if form.is_valid():
            form.save()
            s=upload.objects.all()
            return render(request,'guide/touristplaces.html',{"obj": s})
        else:
            print("form not valied")
            return HttpResponse("un-successfully commented on book")

    else:
        id=request.GET.get('id')
        placename=request.GET.get('placename')
        information=request.GET.get('information')
        package=request.GET.get('package')
        print(placename,information,package)
        data=upload.objects.get(id=id)
        print("data info:",data.information)
        data2 ={'placename':data.placename,'information':data.information,'package':data.package}
        tourismdata=feedbackform(data2)
        return render(request,'user/viewdetails.html',{'tourism':tourismdata,'information':information,'image':data.file})


