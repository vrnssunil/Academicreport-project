from django.conf.urls import url,include
from .views import getstudent,studentsdata,getfaculty,facultiesdata,getsubject,getmathematics,getstudentid,gethppname,getlppname
from .views import getaverage,gethighest,getninty,gettopper,getleast,getmarks,gethpp,getlpp,gethighestname,gettotal
from .rest_api import test,getstudentslist,subject,apimathematics,apiaverage,apileast,apitopper,highestfacultyname,hppfacultyname,lppfacultyname
urlpatterns = [

    url(r'^student/',getstudent),
    url(r'^faculty/',getfaculty),
    url(r'^studentmarks/',studentsdata),
    url(r'^subjectfaculty/',facultiesdata),
#    url(r'^(?P<_subject>[A-Za-z%]+)$', getsubject),
    url(r'^subject/(?P<_subject>[\w\-]+)/$',getsubject),
    url(r'^mathematics/',getmathematics),
    url(r'^average/',getaverage),
    url(r'^studentid/(?P<_id>\d+)', getstudentid),
    url(r'^highest/',gethighest),
    url(r'^ninty/',getninty),
    url(r'^topper/',gettopper),
    url(r'^least/',getleast),
    url(r'^marks/(?P<_marks>\d+)',getmarks),
    url(r'^hpp/',gethpp),
    url(r'^lpp/',getlpp),
    url(r'^highestname/',gethighestname),
    url(r'^total/',gettotal),
    url(r'^hppname/',gethppname),
    url(r'^lppname/',getlppname),
    #rest_api
    url(r'^test/',test),
    url(r'^students/',getstudentslist),
    url(r'^apisubject/(?P<_subject>[\w\-]+)/$',subject),
    url(r'^apimathematics/',apimathematics),
    url(r'^apiaverage/',apiaverage),
    url(r'^apitopper/',apitopper),
    url(r'^apileast/',apileast),
    url(r'^highestfacultyname/',highestfacultyname),
    url(r'^hppfacultyname/',hppfacultyname),
    url(r'^lppfacultyname/',lppfacultyname)
]
'''what ever the function Queries we written in Views.py and Rest_api.py file by using this urls Check out the result in webbrowser with help local of host '''
