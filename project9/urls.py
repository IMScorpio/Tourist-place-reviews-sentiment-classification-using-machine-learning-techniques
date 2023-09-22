"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from user import views as user
from adn import views as admin1
from turstguide import views as guide
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^index/',admin1.index, name="index"),
    url(r'^adminlogin/',admin1.adminlogin, name="adminlogin"),
    url(r'^adminloginaction/',admin1.adminloginaction, name="adminloginaction"),
    url(r'^svm/',admin1.svm, name="svm"),
    url(r'^naviebiase/',admin1.naviebyes, name="naviebiase"),
    url(r'^rf/',admin1.rf,name="rf"),
    url(r'^logout/',admin1.logout,name="logout"),

    url(r'^userlogincheck/',user.userlogincheck,name="userlogincheck"),
    url(r'^userregister/',user.userregister,name="userregister"),
    url(r'^viewuserdata/',user.viewuserdata,name="viewuserdata"),
    url(r'^activateuser/',user.activateuser,name="activateuser"),
    url(r'^userlogin/',user.userlogin,name="userlogin"),
    url(r'^userhome/',user.userhome,name="userhome"),
    url(r'^search/',user.search,name="search"),
    url(r'^usersearchresult1/',user.usersearchresult1,name="usersearchresult1"),
    url(r'^usersearchresult1/',user.usersearchresult1,name="usersearchresult1"),



    url(r'^guidelogin/',guide.guidelogin,name="guidelogin"),
    url(r'^guidelogincheck/',guide.guidelogincheck,name="guidelogincheck"),
    url(r'^guideregister/',guide.guideregister,name="guideregister"),
    url(r'^viewguidedata/',guide.viewguidedata,name="viewguidedata"),
    url(r'^activateguide/',guide.activateguide,name="activateguide"),
    url(r'^guidelogin/',guide.guidelogin,name="guidelogin"),
    url(r'^guidehome/',guide.guidehome,name="guidehome"),
    url(r'^uploaddata/',guide.uploaddata,name="uploaddata"),
    url(r'^touristplaces/',guide.touristplaces,name="touristplaces"),
    url(r'^viewplaces/',guide.viewplaces,name="viewplaces"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









