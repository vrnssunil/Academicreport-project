 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from studentdetails.models import StudentMarks,SubjectFaculty
from django.db.models import Max,Avg,Min,Count,Sum
from django.db.models import Q
from itertools import chain
# Create your views here.
def getstudent(request):
    object = StudentMarks.objects.first()#It just prints studentmarks.object
    return HttpResponse('<H1> ' +str(object)+'</H1>')#print as as string
def getfaculty(request):
    object = SubjectFaculty.objects.first()
    return HttpResponse('<H1> ' +str(object)+'</H1>')
#All students marks data is displayed
def studentsdata(request):
    students = StudentMarks.objects.all()#here StudentMarks.objects is assign to students
    if students:
        context = { #context is used as  a mapping.passed to our template ie index.html
            'students': students
        }
        return render(request, 'index.html', context) #After mapping render combines the both template and context gives the HttpResponse in th given fromat of template in .htmlfile
    else:
        return HttpResponseNotFound("students not found")
#All facultiesdata data  is displayed wrt to their assigned subjects and name of the faculty
def facultiesdata(request):
    faculties = SubjectFaculty.objects.all() #here SubjectFaculty.objects is assign to students
    if faculties:
        context = { #context is used as  a mapping.passed to our template ie index.html
            'faculties': faculties
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("faculties not found")
#It's print subject marks subject given by the user
#filter is used to print the particular subject assing by the user in webbrowser
def getsubject(request,_subject):#passing one of the subject as a parameter
    _subject = _subject.replace('%', ' ')
    students = StudentMarks.objects.filter(subject =_subject)
#ex:suject/Telugu then dat will be printed for Telugu
    if students:
        context = {
            'students': students
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("student not found")
#Query print topper in Mathematics
#It filter the Mathematics from StudentMarks.objects and aggregate(means it analysis the Max marks in bulk of data) and assign to max_marks
#In this filter takes the final data from the above assign max_marks and from that it again max marks of Mathematics assign to students
def getmathematics(request):
    max_marks = StudentMarks.objects.filter(subject='Mathematics').aggregate(Max('marks'))['marks__max']
    students = StudentMarks.objects.filter(marks=max_marks,subject='Mathematics')
    if students:
        context = { #context is used as  a mapping.passed to our template ie index.html
            'students': students
        }
        return render(request, 'index.html', context)#After mapping render combines the both template and context gives the HttpResponse in th given fromat of template in .htmlfile
    else:
        return HttpResponseNotFound("student not found")
#Query prints the particular studentmarks with subject. By user give the input with keyboard as a id(s.no)
def getstudentid(request,_id):#passing one of the id as a parameter
    print (_id)
    students = StudentMarks.objects.filter(id =_id) #filter is used to print the particular id of the in StudentMarks.objects ex:id(s.no=90)it prints that particular id
    if students:
        context = {
            'students': students
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints the average marks of each subject ignores failures
def getaverage(request):
#Query takes the subject values fron StudentMarks.objects and annotate(means average each suject)and filter the marks gte=40
    average=StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40))
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query print faculty with subjectname and count number students got gte=90
def gethighest(request):
    average=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=90)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints gte=90 from StudentMarks
def getninty(request):
    students=StudentMarks.objects.filter(marks__gte=90)
    if students:
        context={
            'students':students
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query pirnts the topper in the total marks of each student
def gettopper(request):
# Here Query takes values of each student,annotate(total sum of each student),order_by prints the data in lowest to highest,so we take reverse order and prints only one value
    total=StudentMarks.objects.all().values('studentname').annotate(total=Sum('marks')).order_by('total').reverse()[:1]
    if total:
        context={
            'total':total
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query pirnts the least in the total marks of each student
def getleast(request):
# Here Query takes values of each student,annotate(total sum of each student),order_by prints the data in lowest to highest and prints only one value
    total=StudentMarks.objects.all().values('studentname').annotate(total=Sum('marks')).order_by('total')[:1]
    if total:
        context={
            'total':total
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints studentmarks.Marks assigned by the  user from keyboard ex:marks/90 gives in webbrowser
def getmarks(request,_marks):#passing or assign marks  as a parameter
#    _marks = _marks.replace('%', ' ')
#Here marks can be filter as user assigned
    students = StudentMarks.objects.filter(marks =_marks)
    if students:
        context = {
            'students': students
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints highest pass percentage of each subject
def gethpp(request):
#Take the values of each subject and count the marks gte=40
    average=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=40)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints highest pass percentage of each subject
def getlpp(request):
#Take the values of each subject and count the marks lte=40
    average=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__lte=40)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query print faculty with subjectname and count number students got gte=90
def gethighestname(request):
#The count number student iterate from StudentMarks.objects gte=90 and assign to f
    f=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=90)
#Here subjects and faculty iterate from SubjectFaculty.objects,order_by is prints lowes to highest
    s=SubjectFaculty.objects.values('name','subject').order_by('name')
#chain is used to commbine to different tables for the w have to import chain from itertools
    average=chain(f,s)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints the total of the each student
def gettotal(request):
#here values taken from StudentMarks.objects sum the individual student total from annotate
    total = StudentMarks.objects.all().values('studentname').annotate(total=Sum('marks'))
    if total:
        context={
            'total':total
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query print faculty with subjectname and count number students got gte=40
def gethppname(request):
#The count number student iterate from StudentMarks.objects gte=40 and assign to r
    r=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=40)
#Here subjects and faculty iterate from SubjectFaculty.objects,order_by is prints lowes to highest
    s=SubjectFaculty.objects.values('name','subject').order_by('name')
#chain is used to commbine to different tables for the w have to import chain from itertools
    average=chain(r,s)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
#Query print faculty with subjectname and count number students got lte=40
def getlppname(request):
#The count number student iterate from StudentMarks.objects lte=90 and assign to v
    v=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__lte=40)
#Here subjects and faculty iterate from SubjectFaculty.objects,order_by is prints lowes to highest
    s=SubjectFaculty.objects.values('name','subject').order_by('name')
#chain is used to commbine to different tables for the w have to import chain from itertools
    average=chain(v,s)
    if average:
        context={
            'average':average
        }
        return render(request,'index.html',context)
    else:
        return HttpResponseNotFound("student not found")
