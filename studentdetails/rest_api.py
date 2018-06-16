#By using this import  we are importing the data from models,serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.core import serializers
from .serializers import StudentMarksSerializer,SubjectFacultySerializer
from .models import StudentMarks,SubjectFaculty
from django.db.models import Max,Avg,Min,Count,Sum
from django.db.models import Q
from django.http import JsonResponse

@api_view(['GET']) #calling api_view by using decorators with help of GET
def test(request):#TEST The function printing in Json format or not
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})
#This function Query is printing the entire StudentMarks in Json fromat from StudentMarks.csv table
@api_view(['GET'])
def getstudentslist(request):
	students = StudentMarks.objects.all() #here StudentMarks.objects is assign to students
	if students:
		serializer = StudentMarksSerializer(students, many=True)
		return Response(serializer.data)#serializer is used to convert the fromat in JsonResponse
	else:
		return Response({"Message": 'student Not Foud'})
#Here we are calling the function to print the student,subject,marks in Json format
@api_view(['GET'])
def subject(request,_subject):#passing one of the subject as a parameter
    _subject = _subject.replace('%', ' ')
    students = StudentMarks.objects.filter(subject =_subject) #filter is used to print the particular subject assing by the user in webbrowser
	#ex:suject/Telugu then dat will be printed for Telugu
    if students:
        serializer = StudentMarksSerializer(students,many=True)#objects are taking from StudentMarksSerializer and assign to serial values
        return Response(serializer.data) #If and else condition
    else:
        return Response({"Message":'Student Not Found'})
#Query prints topper in Mathematics
#It filter the Mathematics from StudentMarks.objects and aggregate(means it analysis the Max marks in bulk of data) and assign to max_marks
#In this filter takes the final data from the above assign max_marks and from that it again max marks of Mathematics assign to students
@api_view(['GET'])
def apimathematics(request):
    max_marks = StudentMarks.objects.filter(subject='Mathematics').aggregate(Max('marks'))['marks__max']#
    students=StudentMarks.objects.filter(marks=max_marks,subject='Mathematics')
    if students:
        serializer = StudentMarksSerializer(students,many=True)
        return Response(serializer.data)

    else:
        return HttpResponseNotFound("student not found")
#Quer prints Average of all subject
#Query of values takes each subject,annotate does total and  average of each subject and filter the gte=40
@api_view(['GET'])
def apiaverage(request):
    average=StudentMarks.objects.all().values('subject').annotate(total=Avg('marks')).filter(Q(marks__gte=40))
    if average:
        context={
            'average':list(average)
        }
        return JsonResponse(context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints Topper of the class in totalmarks
# Here Query takes values of each student,annotate(total sum of each student),order_by prints the data in lowest to highest,so we take reverse order and prints only one value
@api_view(['GET'])
def apitopper(request):
    total=StudentMarks.objects.all().values('studentname').annotate(total=Sum('marks')).order_by('total').reverse()[:1]
    if total:
        context={
            'total':list(total)
        }
        return JsonResponse(context)
    else:
        return HttpResponseNotFound("student not found")
#Query lowest of the class
# Here Query takes values of each student,annotate(total sum of each student),order_by prints the data in lowest to highest and prints only one value
@api_view(['GET'])
def apileast(request):
    total=StudentMarks.objects.all().values('studentname').annotate(total=Sum('marks')).order_by('total')[:1]
    if total:
        context={
            'total':list(total)
        }
        return JsonResponse(context)
    else:
        return HttpResponseNotFound("student not found")
#Query prints highest pass percentage of student,subject,facultyname
@api_view(['GET'])
#The count number student iterate from StudentMarks.objects gte=90.order_by total in highest to lowest because -ve sign  and assign to student
def highestfacultyname(request):
	student=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=90).order_by('-total')
#count takes only first object from the result of student i.e with highest Count
	count=student.first()['subject']
#faculty get name of the first(highest)  faculty name from SubjectFaculty.objects table
	faculty=SubjectFaculty.objects.get(subject=student.first()['subject'])
	context={'faculty with more than 90+ marks':{'subject':faculty.subject,'faculty':faculty.name,'count':student.first()['total']}}
	return JsonResponse(context)
@api_view(['GET'])
def hppfacultyname(request):
#The count number student iterate from StudentMarks.objects gte=40.order_by total in highest to lowest because -ve sign  and assign to student
	hpp=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__gte=40).order_by('-total')
#count takes only first object from the result of student i.e with highest Count
	count=hpp.first()['subject']
#faculty get name of the first(highest)  faculty name from SubjectFaculty.objects table and asssign to faculty
	faculty=SubjectFaculty.objects.get(subject=hpp.first()['subject'])
	context={'faculty with more than 40+marks':{'subject':faculty.subject,'faculty':faculty.name,'count':hpp.first()['total']}}
	return JsonResponse(context)
#The count number student iterate from StudentMarks.objects lte=90.order_by total in highest to lowest because -ve sign  and assign to student
@api_view(['GET'])
def lppfacultyname(request):
	lpp=StudentMarks.objects.all().values('subject').annotate(total=Count('marks')).filter(marks__lte=40).order_by('total')
#count takes only first object from the result of student i.e with highest Count
	count=lpp.first()['subject']
#faculty get name of the first(lowest)  faculty name from SubjectFaculty.objects table and asssign to faculty
	faculty=SubjectFaculty.objects.get(subject=lpp.first()['subject'])
	context={'faculty with less than 40-marks':{'subject':faculty.subject,'faculty':faculty.name,'count':lpp.first()['total']}}
	return JsonResponse(context)
#context defines the print format ie it prints subject,name  from SubjectFaculty.objects table and prints the count value from from the query of result count assign faculty
