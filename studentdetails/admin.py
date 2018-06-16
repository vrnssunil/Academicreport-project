# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentMarks,SubjectFaculty
# Register your models here.
class StudentMarksDetail(admin.ModelAdmin):
    list_display = ('studentname','subject','marks')
admin.site.register(StudentMarks,StudentMarksDetail)
class SubjectFacultyDetail(admin.ModelAdmin):
    list_display = ('subject','name')
admin.site.register(SubjectFaculty,SubjectFacultyDetail)

#It is used to display the table fromat in local host webbrowser
